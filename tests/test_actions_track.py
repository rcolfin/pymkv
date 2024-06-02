from pathlib import Path

import pytest

from pymkv import MKVFile


def test_remove_track_one_track(get_path_test_file: Path) -> None:
    mkv = MKVFile(get_path_test_file)
    mkv.remove_track(1)

    assert len(mkv.tracks) == 1
    assert mkv.tracks[0].track_type == "video"


def test_remove_track_zero_track(get_path_test_file: Path) -> None:
    mkv = MKVFile(get_path_test_file)
    mkv.remove_track(0)

    assert len(mkv.tracks) == 1
    assert mkv.tracks[0].track_type == "audio"


def test_remove_track_and_mux_file(get_base_path: Path, get_path_test_file: Path) -> None:
    mkv = MKVFile(get_path_test_file)
    output_file = get_base_path / "file-test.mkv"
    mkv.remove_track(1)
    mkv.mux(output_file)

    assert output_file.is_file()

    mkv = MKVFile(output_file)

    assert len(mkv.tracks) == 1
    assert mkv.tracks[0].track_type == "video"


def test_move_track_front(get_path_test_file: Path) -> None:
    mkv = MKVFile(get_path_test_file)
    mkv.move_track_front(1)

    assert len(mkv.tracks) == 2  # noqa: PLR2004
    assert mkv.tracks[0].track_type == "audio"
    assert mkv.tracks[1].track_type == "video"


def test_move_track_front_raises(get_path_test_file: Path) -> None:
    mkv = MKVFile(get_path_test_file)

    with pytest.raises(IndexError):
        mkv.move_track_front(-1)

    with pytest.raises(IndexError):
        mkv.move_track_front(2)


def test_move_track_front_and_mux(get_base_path: Path, get_path_test_file: Path) -> None:
    output_file = get_base_path / "file-test.mkv"

    mkv = MKVFile(get_path_test_file)
    mkv.move_track_front(1)
    mkv.mux(output_file)

    mkv = MKVFile(output_file)

    assert len(mkv.tracks) == 2  # noqa: PLR2004
    assert mkv.tracks[0].track_type == "audio"
    assert mkv.tracks[1].track_type == "video"