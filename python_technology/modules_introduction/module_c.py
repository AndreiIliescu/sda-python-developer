# importam tot modulul(fisierul) dar ii dam alt nume
# sintaxa:
# import nume_modul as alt_nume
import module_a as m_a

# cand ne folosim de var/functii din modul:
# alt_nume.Nume_functie

print(m_a.test)

courses = ["Gym", "History", "Math"]
index = m_a.find_index(courses, "Math")
print(index)
