import pytest
from unittest.mock import patch, MagicMock
from main import generate_links

# Mock data for TMDB API response
tmdb_mock_movie = {
    "results": [{"id": 101}],
    "title": "Test Movie",
    "imdb_id": "tt1234567"
}

tmdb_mock_tv = {
    "results": [{"id": 202}],
    "title": "Test Show",
    "imdb_id": "tt7654321"
}


@patch("main.requests.get")
@patch("main.requests.head")
def test_generate_links_movie(mock_head, mock_get):
    mock_head.return_value.status_code = 200

    mock_get.return_value.json.return_value = tmdb_mock_movie

    result = generate_links("Test Movie", "movie")

    assert result["Official Title"] == "Test Movie"
    assert result["TMDB Link"] == "https://www.themoviedb.org/movie/101"
    assert result["IMDb Link"] == "https://www.imdb.com/title/tt1234567/"
    assert result["Rotten Tomatoes Link"].startswith("https://www.rottentomatoes.com/m/")


@patch("main.requests.get")
@patch("main.requests.head")
def test_generate_links_tv(mock_head, mock_get):
    mock_head.return_value.status_code = 404

    mock_get.return_value.json.return_value = tmdb_mock_tv

    result = generate_links("Test Show", "tv")

    assert result["Official Title"] == "Test Show"
    assert result["TMDB Link"] == "https://www.themoviedb.org/tv/202"
    assert result["IMDb Link"] == "https://www.imdb.com/title/tt7654321/"
    assert result["Rotten Tomatoes Link"] == "RT page not found"


def test_generate_links_empty():
    from main import generate_links
    result = generate_links("", "movie")
    assert result == {}
