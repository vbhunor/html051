import pytest
from bs4 import BeautifulSoup
import os

def read_html():
    """Beolvassa az index.html fájlt."""
    if not os.path.exists("index.html"):
        pytest.fail("A 'index.html' fájl nem található!")
    with open("index.html", "r", encoding="utf-8") as f:
        return BeautifulSoup(f, "html.parser")

def test_language():
    """Ellenőrzi, hogy az oldal nyelve magyar-e."""
    soup = read_html()
    assert soup.html.get("lang") == "hu", "Az oldal nyelve nem magyar (hu)."

def test_charset():
    """Ellenőrzi, hogy a karakterkódolás megfelelő-e."""
    soup = read_html()
    meta_tag = soup.find("meta", charset=True)
    assert meta_tag is not None, "Nincs charset meta tag."
    assert meta_tag["charset"].lower() == "utf-8", "A karakterkódolás nem 'utf-8'."

def test_title():
    """Ellenőrzi, hogy a böngésző fülön a 'MIPS' szó jelenik meg."""
    soup = read_html()
    assert soup.title is not None, "Hiányzik a <title> elem."
    assert soup.title.string.strip() == "MIPS", "A title nem 'MIPS'."

def test_headings_and_paragraphs():
    """Ellenőrzi, hogy van-e egyes szintű fejléc és minden bekezdés előtt kettes szintű fejléc."""
    soup = read_html()
    h1 = soup.find("h1")
    assert h1 is not None, "Hiányzik az <h1> fejléc."
    assert h1.text.strip() == "MIPS", "Az <h1> fejléc tartalma nem 'MIPS'."
    
    h2_tags = soup.find_all("h2")
    p_tags = soup.find_all("p")
    assert len(h2_tags) == 4, "Nincs meg minden szükséges <h2> fejléc."
    assert len(p_tags) == 4, "Nincs meg minden szükséges <p> bekezdés."

def test_lists():
    """Ellenőrzi, hogy a harmadik és negyedik bekezdés tartalmát listává alakították-e."""
    soup = read_html()
    ul_tags = soup.find_all("ul")
    assert len(ul_tags) >= 2, "Hiányzik legalább az egyik számozatlan lista."
    
    # Ellenőrzi, hogy a listákban nincsenek csillagok
    for ul in ul_tags:
        assert "*" not in ul.text, "A listákban még mindig vannak csillagok."

def test_bold_text():
    """Ellenőrzi, hogy a 'RISC utasításkészletű' szöveg félkövér-e."""
    soup = read_html()
    strong_tags = soup.find_all("strong")
    bold_texts = [tag.text for tag in strong_tags]
    assert "RISC utasításkészletű" in bold_texts, "A 'RISC utasításkészletű' szöveg nincs félkövérrel jelölve."

def test_comment():
    """Ellenőrzi, hogy a forráskódban szerepel-e megjegyzés a névvel és dátummal."""
    soup = read_html()
    comments = soup.find_all(string=lambda text: isinstance(text, str) and "<!--" in text)
    assert any("nev" in c.lower() and "20" in c for c in comments), "Hiányzik a megjegyzés a névvel és dátummal."

def test_score():
    """Pontozásos rendszer az elkészült feladatok alapján."""
    total_tests = 8
    passed_tests = sum(
        1 for test in [
            test_language,
            test_charset,
            test_title,
            test_headings_and_paragraphs,
            test_lists,
            test_bold_text,
            test_comment
        ]
        if not pytest.raises(Exception, test)
    )
    score = (passed_tests / total_tests) * 100
    print(f"Elért pontszám: {score:.2f}%")
    assert passed_tests == total_tests, "Nem teljesült az összes követelmény."

if __name__ == "__main__":
    pytest.main(["-v", "--disable-warnings"])
