from first_app.models import Genre, Movie
from datetime import datetime, date


g = Genre(name="Action")
g.save()

inception = Movie(
    title="Inception",
    genre=g,
    rating=8,
    released=date(2010, 7, 16),
    description="A thief who steals corporate secrets through dream-sharing technology.",
    created=datetime(2026, 2, 12, 20, 20)
)

inception.save()

c = Genre(name="Comedy")
c.save()

hangover = Movie(
    id=2,
    title="The Hangover",
    genre=c,
    rating=7,
    released=date(2009, 6, 2),
    description="Three groomsmen lose the bride's husband after a wild bachelor party.",
    created=datetime(2026, 2, 12, 20, 20)
)

hangover.save()

d=Genre(name="Drama")
d.save()

godfather = Movie(
    id=3,
    title="The Godfather",
    genre=d,
    rating=9,
    released=date(1972, 3, 24),
    description="The aging patriarch of an organized crime dynasty transfers control.",
    created=datetime(2026, 2, 12, 20, 20)
)

godfather.save()
