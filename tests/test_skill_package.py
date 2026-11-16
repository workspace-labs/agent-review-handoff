"""Offline integrity checks for the shipped skill, using only Python's stdlib.

Run from the repository root:  python3 -m unittest discover tests

These verify the package's wiring. Whether an agent reviews well with the skill
is exercised separately, by the cases in behavioral-cases.md.
"""

from pathlib import Path
import re
import unittest

REPO = Path(__file__).resolve().parents[1]
SKILL = REPO / "skills" / "independent-review-handoff"
LINK = re.compile(r"\[[^\]\n]*\]\(([^)\n]+)\)")


def local_links(path):
    """Relative file targets of the markdown links in one file, anchors dropped."""
    for target in LINK.findall(path.read_text(encoding="utf-8")):
        if not re.match(r"^[a-z]+:|^#", target):
            yield target.split("#")[0]


class SkillPackage(unittest.TestCase):
    def setUp(self):
        self.text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        self.frontmatter = self.text.split("---\n")[1]

    def test_name_matches_folder(self):
        self.assertIn("name: {}\n".format(SKILL.name), self.frontmatter)

    def test_description_fits_the_skill_contract(self):
        description = re.search(r'^description: "(.*)"$', self.frontmatter, re.M)
        self.assertIsNotNone(description, "description must be one double-quoted line")
        self.assertLessEqual(len(description[1]), 1024)

    def test_every_local_link_resolves(self):
        for source in [SKILL / "SKILL.md", *sorted((SKILL / "references").glob("*.md"))]:
            for target in local_links(source):
                self.assertTrue((source.parent / target).is_file(),
                                "{} links to missing {}".format(source.name, target))

    def test_every_reference_file_is_reachable_from_the_skill(self):
        linked = {(SKILL / target).resolve() for target in local_links(SKILL / "SKILL.md")}
        for reference in sorted((SKILL / "references").glob("*.md")):
            self.assertIn(reference.resolve(), linked,
                          "{} is never linked from SKILL.md".format(reference.name))

    def test_version_matches_the_changelog(self):
        skill = re.search(r"^Skill version: (\d+\.\d+\.\d+)$", self.text, re.M)
        changelog = re.search(r"^## (\d+\.\d+\.\d+) ", (REPO / "CHANGELOG.md").read_text(encoding="utf-8"), re.M)
        self.assertIsNotNone(skill, "SKILL.md must carry a 'Skill version:' line")
        self.assertEqual(skill[1], changelog[1])


if __name__ == "__main__":
    unittest.main()
