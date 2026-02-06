import os
import re
import subprocess
import sys

# -----------------------------
# Réglages généraux
# -----------------------------
IGNORE_PROMPTS = True

PROMPT_INLINE_RE = re.compile(
    r"(?:^|\n)?\s*(?:Entrez|Veuillez entrer)[^:\n]*:\s*",
    flags=re.IGNORECASE
)

def clean_output(s: str) -> str:
    s = s.replace("\r\n", "\n")
    if IGNORE_PROMPTS:
        for _ in range(5):
            new_s = PROMPT_INLINE_RE.sub("", s)
            if new_s == s:
                break
            s = new_s
        lines = [l for l in s.split("\n") if l.strip()]
        s = "\n".join(lines)
        if s and not s.endswith("\n"):
            s += "\n"
    return s

def run_script(filename: str, input_data: str) -> str | None:
    try:
        completed = subprocess.run(
            [sys.executable, filename],
            input=input_data,
            text=True,
            encoding="utf-8",
            capture_output=True,
            timeout=2,
            env=dict(os.environ, PYTHONIOENCODING="utf-8")
        )
        return clean_output(completed.stdout)
    except Exception:
        return None

def test_equal(filename, input_data, expected):
    out = run_script(filename, input_data)
    return out == expected

# ============================================================
# EXO 1 - Bilan de visionnage Carabins
# ============================================================
exo1_ok = 0

exo1_ok += test_equal("exo1.py",
    "Adem Hmissa\n3\n120\n2\n95\n",
    "Bonjour Adem Hmissa\n"
    "Football (Carabins): 3 match(s), 6h00 de visionnage\n"
    "Soccer (Carabins): 2 match(s), 3h10 de visionnage\n"
    "Total: 9h10\n"
)

exo1_ok += test_equal("exo1.py",
    "Alice\n0\n90\n1\n60\n",
    "Bonjour Alice\n"
    "Football (Carabins): 0 match(s), 0h00 de visionnage\n"
    "Soccer (Carabins): 1 match(s), 1h00 de visionnage\n"
    "Total: 1h00\n"
)

exo1_ok += test_equal("exo1.py",
    "Bob\n1\n0\n1\n60\n",
    "Erreur - donnees invalides.\n"
)

exo1_ok += test_equal("exo1.py",
    "Frank\n2\n180\n3\n120\n",
    "Bonjour Frank\n"
    "Football (Carabins): 2 match(s), 6h00 de visionnage\n"
    "Soccer (Carabins): 3 match(s), 6h00 de visionnage\n"
    "Total: 12h00\n"
)

exo1_ok += test_equal("exo1.py",
    "Isabelle\nabc\n90\n1\n60\n",
    "Erreur - donnees invalides.\n"
)

print(f"exo 1 : {exo1_ok} sur 5 tests réussis")

# ============================================================
# EXO 2 - Ambiance autour du stade
# ============================================================
exo2_ok = 0

exo2_ok += test_equal("exo2.py",
    "0\n0\n0\n0\n0\n0\n0\n0\n",
    "10 | . . . . . . . .\n"
    " 9 | . . . . . . . .\n"
    " 8 | . . . . . . . .\n"
    " 7 | . . . . . . . .\n"
    " 6 | . . . . . . . .\n"
    " 5 | . . . . . . . .\n"
    " 4 | . . . . . . . .\n"
    " 3 | . . . . . . . .\n"
    " 2 | . . . . . . . .\n"
    " 1 | . . . . . . . .\n"
    "     A B C D E F G H\n"
)

exo2_ok += test_equal("exo2.py",
    "100\n0\n0\n0\n0\n0\n0\n100\n",
    "10 | ❚ . . . . . . ❚\n"
    " 9 | ❚ . . . . . . ❚\n"
    " 8 | ❚ . . . . . . ❚\n"
    " 7 | ❚ . . . . . . ❚\n"
    " 6 | ❚ . . . . . . ❚\n"
    " 5 | ❚ . . . . . . ❚\n"
    " 4 | ❚ . . . . . . ❚\n"
    " 3 | ❚ . . . . . . ❚\n"
    " 2 | ❚ . . . . . . ❚\n"
    " 1 | ❚ . . . . . . ❚\n"
    "     A B C D E F G H\n"
)

exo2_ok += test_equal("exo2.py",
    "-1\n0\n0\n0\n0\n0\n0\n0\n",
    "Erreur - donnees invalides.\n"
)

exo2_ok += test_equal("exo2.py",
    "0\n0\n0\n100\n0\n0\n0\n0\n",
    "10 | . . . ❚ . . . .\n"
    " 9 | . . . ❚ . . . .\n"
    " 8 | . . . ❚ . . . .\n"
    " 7 | . . . ❚ . . . .\n"
    " 6 | . . . ❚ . . . .\n"
    " 5 | . . . ❚ . . . .\n"
    " 4 | . . . ❚ . . . .\n"
    " 3 | . . . ❚ . . . .\n"
    " 2 | . . . ❚ . . . .\n"
    " 1 | . . . ❚ . . . .\n"
    "     A B C D E F G H\n"
)

exo2_ok += test_equal("exo2.py",
    "75\n50\n25\n10\n15\n30\n55\n80\n",
    "10 | . . . . . . . ❚\n"
    " 9 | ❚ . . . . . . ❚\n"
    " 8 | ❚ . . . . . . ❚\n"
    " 7 | ❚ . . . . . . ❚\n"
    " 6 | ❚ ❚ . . . . ❚ ❚\n"
    " 5 | ❚ ❚ . . . . ❚ ❚\n"
    " 4 | ❚ ❚ . . . . ❚ ❚\n"
    " 3 | ❚ ❚ ❚ . . ❚ ❚ ❚\n"
    " 2 | ❚ ❚ ❚ . . ❚ ❚ ❚\n"
    " 1 | ❚ ❚ ❚ ❚ ❚ ❚ ❚ ❚\n"
    "     A B C D E F G H\n"
)

print(f"exo 2 : {exo2_ok} sur 5 tests réussis")

# ============================================================
# EXO 3 - Choisir le meilleur trajet vers le CEPSUM
# ============================================================
exo3_ok = 0

exo3_ok += test_equal("exo3.py",
    "1\n10\n12\n3\n",
    "Egalite : marcher et metro.\n"
)

exo3_ok += test_equal("exo3.py",
    "0.2\n0\n20\n0\n",
    "Option la plus rapide : navette.\n"
)

exo3_ok += test_equal("exo3.py",
    "0\n0\n0\n0\n",
    "Egalite : marcher, navette et metro.\n"
)

exo3_ok += test_equal("exo3.py",
    "5\n15\n10\n2\n",
    "Option la plus rapide : metro.\n"
)

exo3_ok += test_equal("exo3.py",
    "-1\n10\n12\n3\n",
    "Erreur - donnees invalides.\n"
)

print(f"exo 3 : {exo3_ok} sur 5 tests réussis")

# ============================================================
# EXO 4 - Vérification d'une rampe d'accessibilité
# ============================================================
exo4_ok = 0

exo4_ok += test_equal("exo4.py",
    "40\n6\n",
    "Pente: 6.67%\n"
    "Angle: 3.81 deg\n"
    "Conforme: OUI\n"
)

exo4_ok += test_equal("exo4.py",
    "80\n5\n",
    "Pente: 16.00%\n"
    "Angle: 9.09 deg\n"
    "Conforme: NON\n"
    "Depassement: 8.00%\n"
)

exo4_ok += test_equal("exo4.py",
    "0\n10\n",
    "Pente: 0.00%\n"
    "Angle: 0.00 deg\n"
    "Conforme: OUI\n"
)

exo4_ok += test_equal("exo4.py",
    "200\n5\n",
    "Pente: 40.00%\n"
    "Angle: 21.80 deg\n"
    "Conforme: NON\n"
    "Depassement: 32.00%\n"
)

exo4_ok += test_equal("exo4.py",
    "-1\n5\n",
    "Erreur - donnees invalides.\n"
)

print(f"exo 4 : {exo4_ok} sur 5 tests réussis")

# ============================================================
# EXO 5 - Planification d'achat de billets
# ============================================================
exo5_ok = 0

exo5_ok += test_equal("exo5.py",
    "0\nN\n",
    "Forfaits de 24 billets - 0\n"
    "Forfaits de 12 billets - 0\n"
    "Forfaits de 5 billets - 0\n"
    "Billets unitaires - 0\n"
    "Total billets - 0\n"
    "Prix total - 0.00$\n"
)

exo5_ok += test_equal("exo5.py",
    "13\nN\n",
    "Forfaits de 24 billets - 0\n"
    "Forfaits de 12 billets - 1\n"
    "Forfaits de 5 billets - 0\n"
    "Billets unitaires - 1\n"
    "Total billets - 13\n"
    "Prix total - 39.60$\n"
)

exo5_ok += test_equal("exo5.py",
    "89\nO\n",
    "Forfaits de 24 billets - 3\n"
    "Forfaits de 12 billets - 1\n"
    "Forfaits de 5 billets - 1\n"
    "Billets unitaires - 0\n"
    "Total billets - 89\n"
    "Prix total - 219.78$\n"
)

exo5_ok += test_equal("exo5.py",
    "5\nO\n",
    "Forfaits de 24 billets - 0\n"
    "Forfaits de 12 billets - 0\n"
    "Forfaits de 5 billets - 1\n"
    "Billets unitaires - 0\n"
    "Total billets - 5\n"
    "Prix total - 13.86$\n"
)

exo5_ok += test_equal("exo5.py",
    "10\nX\n",
    "Erreur - donnees invalides.\n"
)

print(f"exo 5 : {exo5_ok} sur 5 tests réussis")

# ============================================================
# Résumé
# ============================================================
total = exo1_ok + exo2_ok + exo3_ok + exo4_ok + exo5_ok
print("=" * 60)
print(f"TOTAL: {total} sur 25 tests réussis")
print("=" * 60)
