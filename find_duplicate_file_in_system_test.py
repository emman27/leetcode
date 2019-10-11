from find_duplicate_file_in_system import Directory, File


def test_file_from_string():
    f = File.from_str("1.txt(abcd)", '')
    assert "1.txt" == f.name
    assert "abcd" == f.content
    assert '' == f.path


def test_directory_from_string():
    d = Directory.from_str("root/a 1.txt(abcd) 2.txt(efgh)")
    assert 2 == len(d.files)
    assert "root/a" == d.path
    assert "abcd" == d.files[0].content
    assert "1.txt" == d.files[0].name
