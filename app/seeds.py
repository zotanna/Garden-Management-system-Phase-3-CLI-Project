from app import app
from models import db, Plant, Gardener, Garden

if __name__ == '__main__':
    with app.app_context():

        # SQLAlchemy seeding

        # Clear out models
        Plant.query.delete()
        Gardener.query.delete()
        Garden.query.delete()

        plants = [
            Plant(
                name="Sukuma Wiki",
                species="Brassica oleracea",
                season="Year-round",
                harvest_time=8
            ),
            Plant(
                name="Maize",
                species="Zea mays",
                season="Rainy season",
                harvest_time=90
            ),
            Plant(
                name="Kales",
                species="Brassica oleracea",
                season="Cool season",
                harvest_time=60
            ),
            Plant(
                name="Tomatoes",
                species="Solanum lycopersicum",
                season="Year-round",
                harvest_time=12
            ),
            Plant(
                name="Capsicum",
                species="Capsicum annuum",
                season="Year-round",
                harvest_time=10
            )
        ]

        db.session.add_all(plants)

        gardeners = [
            Gardener(
                name="John Kamau",
                location="Nairobi",
                experience=5
            ),
            Gardener(
                name="Jane Muthoni",
                location="Eldoret",
                experience=3
            ),
            Gardener(
                name="David Gitonga",
                location="Mombasa",
                experience=4
            ),
            Gardener(
                name="Mary Wanjiku",
                location="Kisumu",
                experience=2
            ),
            Gardener(
                name="Peter Maina",
                location="Nakuru",
                experience=1
            )
        ]

        db.session.add_all(gardeners)

        gardens = [
            Garden(
                name="Green Oasis",
                location="Nairobi",
                experience_req=5,
                plant_id=1,
                gardener_id=1
            ),
            Garden(
                name="Maize Haven",
                location="Eldoret",
                experience_req=3,
                plant_id=2,
                gardener_id=2
            ),
            Garden(
                name="Coastal Garden",
                location="Mombasa",
                experience_req=4,
                plant_id=4,
                gardener_id=3
            ),
            Garden(
                name="Lakefront Farm",
                location="Kisumu",
                experience_req=2,
                plant_id=3,
                gardener_id=4
            ),
            Garden(
                name="Highland Paradise",
                location="Nakuru",
                experience_req=1,
                plant_id=5,
                gardener_id=5
            )
        ]

        db.session.add_all(gardens)

        db.session.commit()
