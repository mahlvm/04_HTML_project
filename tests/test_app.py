from playwright.sync_api import Page, expect

def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed("seeds/record_store.sql")
    page.goto (f"http://{test_web_address}/albums")
    li_tags = page.locator("li")
    expect (li_tags).to_have_text ([
        "Doolittle",
        "Surfer Rosa",
    ])


def test_get_albums_just_one(page, test_web_address, db_connection):
    db_connection.seed("seeds/record_store.sql")
    page.goto (f"http://{test_web_address}/artists/1")
    h1_tags = page.locator("h1")
    p_tags = page.locator("p")
    expect (h1_tags).to_have_text ([
        "Doolittle"
    ])
    expect (p_tags).to_have_text ([
        'Release year:1989',
        'Artist: Pixies'
    ])
    

def test_visit_album_show_page(page, test_web_address, db_connection):
    db_connection.seed("seeds/record_store.sql")
    page.goto (f"http://{test_web_address}/albums")
    page.wait_for_load_state("load")
    page.click("text=Surfer Rosa")
    h1_tag = page.locator("h1")
    expect (h1_tag).to_have_text("Album: Surfer Rosa")
    release_year_tag = page.locator(".t-release-year")
    expect(release_year_tag).to_have_text("Released: 1988")



def test_visit_album_show_page_and_go_back(page, test_web_address, db_connection):
    db_connection.seed("seeds/record_store.sql")
    page.goto (f"http://{test_web_address}/albums")
    page.click("text=Surfer Rosa")
    page.click("text=Go back to the album list")
    h1_tag = page.locator("h1")
    expect (h1_tag).to_have_text("Albums")

