from playwright.sync_api import Page, expect

def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed("seeds/record_store.sql")
    page.goto (f"http://{test_web_address}/albums")
    div_tags = page.locator("div")
    expect (div_tags).to_have_text ([
        "Title: Doolittle\nReleased: 1989",
        "Title: Surfer Rosa\nReleased: 1988"
])

# def test_get_artists(page, test_web_address, db_connection):
#     db_connection.seed("seeds/record_store.sql")
#     page.goto (f"http://{test_web_address}/artists")
#     div_tags = page.locator("h1")
#     expect (div_tags).to_have_text ([
#         "Title: Doolittle\nReleased: 1989",
#         "Title: Surfer Rosa\nReleased: 1988"
# ])


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
    





# # Tests for your routes go here

# # === Example Code Below ===

# """
# We can get an emoji from the /emoji page
# """
# def test_get_emoji(page, test_web_address): # Note new parameters
#     # We load a virtual browser and navigate to the /emoji page
#     page.goto(f"http://{test_web_address}/emoji")

#     # We look at the <strong> tag
#     strong_tag = page.locator("strong")

#     # We assert that it has the text ":)"
#     expect(strong_tag).to_have_text(":)")

# # === End Example Code ===

# # def test_get_hello(page, test_web_adress):
# #     page.goto(f"http://{test_web_adress}/hello")
# #     heading_tag = page.locator("h1")
# #     expect(heading_tag).to_have_text("Hello, world")

# def test_get_goodbye(page, test_web_address):
#     page.goto(f"http://{test_web_address}/goodbye")
#     strong_tag = page.locator("strong")
#     expect(strong_tag).to_have_text("Bye!")