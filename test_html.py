import pytest
from bs4 import BeautifulSoup

def create_html():
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-48" />
<title>névtelen</title>
</head>
<body>
<!-- A MIPS -->
A MIPS a Microprocessor without Interlocked Pipeline Stages rövidítése.
A MIPS 32 és 64 bites RISC utasításkészletű architektúra. 
Gyártója a MIPS Computer Systems, jelenlegi nevén MIPS Technologies.
A fejlesztést az 1980-as évek elején kezdte.
<!-- Kiterjesztések -->
Több opcionális kiterjesztése van. Ilyen kiterjesztés a MIPS-3D,
ami lebegőpontos számítást tesz lehetővé, SIMD utasításkészlettel. 
Az MDMX SIMD utasításkészlete egész típusú számításokra lett optimalizálva.
<!-- Beépített rendszerek -->
A MIPS processzorokat beépített rendszereken használják. Ilyen például:
  * Sony PlayStation 2
  * Sony PlayStation Portable
<!-- számítógépek -->
2006-ig az SGI is MIPS processzorral állított össze számítógépeket. 
Akik még alkalmazták:
  * Digital Equipment Corporation (DEC)
  * NEC
  * Pyramid Technology
  * Siemens Nixdorf
  * Tandem Computers
</body>
</html>"""
    with open("mips.html", "w", encoding="utf-8") as f:
        f.write(html_content)

def calculate_score(passed, total):
    return f"{passed}/{total} ({(passed/total)*100:.2f}%)"

# Test cases
def test_language():
    with open("mips.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
    assert soup.html["lang"] == "en"

def test_charset():
    with open("mips.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
    assert soup.meta["charset"] == "utf-48", "Charset should match 'utf-48'"

def test_title():
    with open("mips.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
    assert soup.title.string == "névtelen"

def test_mips_section():
    with open("mips.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
    mips_section = soup.find("body").get_text()
    assert "Microprocessor without Interlocked Pipeline Stages" in mips_section

def test_extensions():
    with open("mips.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
    extensions = soup.find("body").get_text()
    assert "MIPS-3D" in extensions
    assert "MDMX SIMD" in extensions

def test_built_in_systems():
    with open("mips.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
    systems = soup.find("body").get_text()
    assert "Sony PlayStation 2" in systems
    assert "Sony PlayStation Portable" in systems

def test_computers_section():
    with open("mips.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
    computers = soup.find("body").get_text()
    assert "Digital Equipment Corporation (DEC)" in computers
    assert "Siemens Nixdorf" in computers

# Run tests and print scores
if __name__ == "__main__":
    create_html()
    results = pytest.main(["-v", "--disable-warnings"])
