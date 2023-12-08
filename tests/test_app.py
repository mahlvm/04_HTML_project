from playwright.sync_api import Page, expect

def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed("seeds/record_store.sql")
    page.goto (f"http://{test_web_address}/albums")
    li_tags = page.locator("li")
    expect (li_tags).to_have_text ([
        "Doolittle",
        "Surfer Rosa",
    ])

def test_visit_album_show_page(page, test_web_address, db_connection):
    db_connection.seed("seeds/record_store.sql")
    page.goto (f"http://{test_web_address}/albums")
    page.wait_for_load_state("load")
    page.click("text=Surfer Rosa")
    h1_tag = page.locator("h1")
    expect (h1_tag).to_have_text("Album: Surfer Rosa")
    release_year_tag = page.locator(".t-release-year")
    expect(release_year_tag).to_have_text("Release: 1988")



def test_visit_album_show_page_and_go_back(page, test_web_address, db_connection):
    db_connection.seed("seeds/record_store.sql")
    page.goto (f"http://{test_web_address}/albums")
    page.click("text=Surfer Rosa")
    page.click("text=Go back to the album list")
    h1_tag = page.locator("h1")
    expect (h1_tag).to_have_text("Albums")




def test_get_artist(page, test_web_address, db_connection):
    db_connection.seed("seeds/record_store.sql")
    page.goto (f"http://{test_web_address}/artists")
    li_tags = page.locator("li")
    expect (li_tags).to_have_text ([
        'Pixies',
        'ABBA',
        'Taylor Swift',
        'Nina Simone',
    ])


def test_visit_artist_show_page(page, test_web_address, db_connection):
    db_connection.seed("seeds/record_store.sql")
    page.goto (f"http://{test_web_address}/artists")
    page.click("text=Pixies")
    h1_tag = page.locator("h1")
    expect (h1_tag).to_have_text("Artist: Pixies")
    genre_tag = page.locator(".t-genre")
    expect(genre_tag).to_have_text("Genre: Rock")


def test_visit_artist_show_page_and_go_back(page, test_web_address, db_connection):
    db_connection.seed("seeds/record_store.sql")
    page.goto (f"http://{test_web_address}/artists")
    page.click("text=Pixies")
    page.click("text=Go back to the album list")
    h1_tag = page.locator("h1")
    expect (h1_tag).to_have_text("Artists")



def test_create_album(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed("seeds/record_store.sql")
    page.goto (f"http://{test_web_address}/albums")
    page.click('text="Add album"')
    page.fill('input[name=title]', "Test Album")
    page.fill('input[name=release_year]', "1234")
    page.click('text="Add album"')
    h1_tag = page.locator("h1")
    expect (h1_tag).to_have_text("Album: Test Album")
    release_year_tag = page.locator(".t-release-year")
    expect (release_year_tag).to_have_text("Release: 1234")

######

def test_validate_album(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed("seeds/record_store.sql")
    page.goto (f"http://{test_web_address}/albums")
    page.click('text="Add album"')
    page.click('text="Add album"')
    errors_tag = page.locator(".t-errors")
    expect (errors_tag).to_have_text(
        "Your submition contains errors: " \
        "Title must not be blank, " \
        "Release year must be a number" 

    )

######

def test_create_artist(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed("seeds/record_store.sql")
    page.goto (f"http://{test_web_address}/artists")
    page.click('text="Add artist"')
    page.fill('input[name=name]', "Artist Name")
    page.fill('input[name=genre]', "Genre Test")
    page.click('text="Add artist"')
    h1_tag = page.locator("h1")
    expect (h1_tag).to_have_text("Artist: Artist Name")
    genre_tag = page.locator(".t-genre")
    expect (genre_tag).to_have_text("Genre: Genre Test")

######

def test_validate_artist(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed("seeds/record_store.sql")
    page.goto (f"http://{test_web_address}/artists")
    page.click('text="Add artist"')
    page.click('text="Add artist"')
    errors_tag = page.locator(".t-errors")
    expect (errors_tag).to_have_text(
        "Your submition contains errors: " \
        "Name must not be blank, " \
        "Genre must not be blank" 

    )