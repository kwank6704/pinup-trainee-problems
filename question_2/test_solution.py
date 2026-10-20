import unittest

from solution import FileExplorer


class FileExplorerTest(unittest.TestCase):
    def test_starts_at_root_empty(self):
        fe = FileExplorer()
        self.assertEqual(fe.cwd(), "/")
        self.assertEqual(fe.ls(), "")

    def test_mkdir_and_touch(self):
        fe = FileExplorer()
        fe.mkdir("usr")
        fe.touch("notes.txt")
        self.assertEqual(fe.ls(), "notes.txt usr")

    def test_mkdir_already_exists(self):
        fe = FileExplorer()
        fe.mkdir("usr")
        self.assertEqual(fe.mkdir("usr"), "usr already exists.")

    def test_touch_already_exists(self):
        fe = FileExplorer()
        fe.touch("a.txt")
        self.assertEqual(fe.touch("a.txt"), "a.txt already exists.")

    def test_cd_not_found(self):
        fe = FileExplorer()
        self.assertEqual(fe.cd("random"), "random not found.")

    def test_cd_into_file_is_rejected(self):
        fe = FileExplorer()
        fe.touch("readme.md")
        self.assertEqual(fe.cd("readme.md"), "readme.md is not a directory.")

    def test_cd_up_from_root(self):
        fe = FileExplorer()
        self.assertEqual(fe.cd(".."), "currently at root.")

    def test_cd_relative_then_up(self):
        fe = FileExplorer()
        fe.mkdir("usr")
        fe.cd("usr")
        self.assertEqual(fe.cwd(), "/usr")
        fe.cd("..")
        self.assertEqual(fe.cwd(), "/")

    def test_cd_multi_segment_path_from_root(self):
        fe = FileExplorer()
        fe.mkdir("usr")
        fe.cd("usr")
        fe.mkdir("share")
        fe.cd("/usr/share")
        self.assertEqual(fe.cwd(), "/usr/share")

    def test_cd_failure_does_not_move(self):
        fe = FileExplorer()
        fe.mkdir("usr")
        fe.cd("usr")
        fe.cd("nope")  # should fail and leave current dir unchanged
        self.assertEqual(fe.cwd(), "/usr")

    def test_pdf_example_sequence(self):
        fe = FileExplorer()
        self.assertEqual(fe.ls(), "")
        self.assertIsNone(fe.mkdir("usr"))
        self.assertEqual(fe.cd("random"), "random not found.")
        self.assertIsNone(fe.cd("usr"))
        self.assertIsNone(fe.touch("readme.md"))
        self.assertIsNone(fe.mkdir("share"))
        self.assertEqual(fe.ls(), "readme.md share")
        self.assertEqual(fe.cd("readme.md"), "readme.md is not a directory.")
        self.assertIsNone(fe.cd("share"))
        self.assertEqual(fe.cwd(), "/usr/share")
        self.assertIsNone(fe.cd(".."))
        self.assertEqual(fe.cwd(), "/usr")
        self.assertIsNone(fe.cd("/usr/share"))
        self.assertEqual(fe.cwd(), "/usr/share")


if __name__ == "__main__":
    unittest.main()
