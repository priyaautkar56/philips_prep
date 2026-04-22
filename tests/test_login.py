import pytest
from playwright.sync_api import Page, expect

def test_valid_login(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")
    page.locator("button[type='submit']").click()
    expect(page.locator(".flash.success")).to_be_visible()

def test_invalid_login(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("wrongpassword")
    page.locator("button[type='submit']").click()
    expect(page.locator(".flash.error")).to_be_visible()
    expect(page.locator(".flash.error")).to_contain_text("Your password is invalid")  

def test_invalid_login(page: Page):
    page.goto("https://the-internet.herokuapp.com/login") 
    page.locator("#username").fill("priya") 
    page.locator("#password").fill("mypassword")
    page.locator("button[type='submit']").click()
    expect(page.locator("#flash")).to_be_visible()
    print(page.locator(".flash.error").inner_text())
    expect(page.locator(".flash.error")).to_contain_text('Your username is invalid!')

def test_forgot_password(page: Page):
    page.goto("https://the-internet.herokuapp.com/forgot_password")
    page.locator("#email").fill("priya@test.com")
    page.locator("#form_submit").click()
    expect(page.locator("#content")).to_contain_text("Your e-mail's been sent!")