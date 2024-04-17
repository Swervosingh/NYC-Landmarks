

# Standard library imports
from random import randint, choice as rc
from app import app
from models import db, Landmarks
# Remote library imports
with app.app_context():
    db.drop_all()
    db.create_all()
    
    landmarks = [
        Landmarks(
            name='Empire State Building',
            description='A skyscraper located in Midtown Manhattan, New York City. It has a total height of 1,454 feet (443.2 meters), including its antenna.',
            image_url='https://www.esbnyc.com/sites/default/files/2020-01/ESB%20Day.jpg'
        ),
        Landmarks(
            name='Brooklyn Bridge',
            description='A hybrid cable-stayed/suspension bridge in New York City, spanning the East River between the boroughs of Manhattan and Brooklyn. It is one of the oldest roadway bridges in the United States.',
            image_url='https://cdn.britannica.com/80/115080-050-46BE2B70/Brooklyn-Bridge-East-River-New-York-City.jpg'
        ),
        Landmarks(
            name='The High Line',
            description='A 1.45-mile-long (2.33 km) elevated linear park, greenway, and rail trail created on a former New York Central Railroad spur on the west side of Manhattan in New York City.',
            image_url='https://upload.wikimedia.org/wikipedia/commons/5/56/AHigh_Line_Park%2C_Section_1a.jpg'
        ),
        Landmarks(
            name='Central Park',
            description='An urban park in New York City located between the Upper West and Upper East Sides of Manhattan. It is the fifth-largest park in the city by area, covering 843 acres (341 ha).',
            image_url='https://park.marmaranyc.com/hs-fs/hubfs/Explore%20Widget/Central%20Park.jpg?width=2000&height=1333&name=Central%20Park.jpg'
        ),
        Landmarks(
            name='Times Square',
            description='A major commercial intersection, tourist destination, entertainment center, and neighborhood in the Midtown Manhattan section of New York City, at the junction of Broadway and Seventh Avenue.',
            image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/New_york_times_square-terabass.jpg/640px-New_york_times_square-terabass.jpg'
        ),
        Landmarks(
            name='Statue of Liberty',
            description='A colossal neoclassical sculpture on Liberty Island in New York Harbor in New York City, in the United States. The copper statue, a gift from the people of France to the people of the United States, was designed by French sculptor Frédéric Auguste Bartholdi and its metal framework was built by Gustave Eiffel.',
            image_url='https://cdn.britannica.com/71/99571-050-DFF0A6E5/Statue-of-Liberty-Island-New-York.jpg'
        ),
        Landmarks(
            name='One World Trade Center',
            description='The main building of the rebuilt World Trade Center complex in Lower Manhattan, New York City. It is the tallest building in the Western Hemisphere, and the sixth-tallest in the world.',
            image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/One_World_Trade_Center_%28cropped_9_to_16%29.jpg/250px-One_World_Trade_Center_%28cropped_9_to_16%29.jpg'
        ),
        Landmarks(
            name='Rockefeller Center',
            description='A large complex consisting of 19 commercial buildings covering 22 acres (89,000 m2) between 48th Street and 51st Street in Midtown Manhattan, New York City.',
            image_url='https://images.ctfassets.net/xxo9lvoc4mg6/4K5L9O2vfoeI4BVBXwgKOJ/cf9ededba514318f773f56448d984993/45729267_2128908227130165_8989343804381200384_o.jpg?w=2000&q=90'
        ),
        Landmarks(
            name='The Metropolitan Museum of Art',
            description='The largest art museum in the United States, and is among the most visited art museums in the world. It was founded to bring art to the American people.',
            image_url='https://cdn.sanity.io/images/cctd4ker/production/b8a5e07c166342e1c7f6fe30b8c45d64fea69ea5-4096x2326.jpg?w=3840&q=75&fit=clip&auto=format'
        ),
        Landmarks(
            name='The Museum of Modern Art',
            description='An art museum located in Midtown Manhattan in New York City, on 53rd Street between Fifth and Sixth Avenues. It plays a major role in developing and collecting modern art.',
            image_url='https://example.com/the_museum_of_modern_art.jpg'
        ),
        Landmarks(
            name='The Guggenheim Museum',
            description='An art museum located at 1071 Fifth Avenue on the corner of East 89th Street in the Upper East Side neighborhood of Manhattan, New York City.',
            image_url='https://www.guggenheim.org/wp-content/uploads/2016/04/architecture-srgm-exterior-flavin-16-9-ratio-web.jpg'
        ),
        Landmarks(
            name='The American Museum of Natural History',
            description='A natural history museum on the Upper West Side of Manhattan in New York City. In Theodore Roosevelt Park, across the street from Central Park.',
            image_url='https://media.cntraveler.com/photos/5a7746e0aeb19b5730310bf7/16:9/w_2560,c_limit/Museum-of-Natural-History_AMNHD.-Finnin_2018_4.-Afr.jpg'
        ),
        Landmarks(
            name='The Bronx Zoo',
            description='The largest metropolitan zoo in the United States and among the largest in the world. It is one of the largest wildlife conservation parks in the country.',
            image_url='https://upload.wikimedia.org/wikipedia/commons/7/7a/Bronx_Zoo_001.jpg'
        ),
        Landmarks(
            name='Coney Island',
            description='A residential neighborhood, peninsula and beach on the Atlantic Ocean in southwestern Brooklyn, New York City. The site of amusement parks and a seaside resort.',
            image_url='https://cdn.shopify.com/s/files/1/0594/6078/0229/products/Coney_Island_Amusement_Park__New_York_City.jpg?v=1660415483'
        ),
        Landmarks(
            name='Yankee Stadium',
            description='A baseball park located in Concourse, Bronx, New York City. It is the home field for the New York Yankees of Major League Baseball, and New York City FC of Major League Soccer.',
            image_url='https://upload.wikimedia.org/wikipedia/commons/6/68/Yankee_Stadium_aerial_from_Blackhawk.jpg'
        ),
        Landmarks(
            name='Madison Square Garden',
            description='A multi-purpose indoor arena in New York City. Located in Midtown Manhattan between Seventh and Eighth Avenues from 31st to 33rd Streets, it is situated atop Pennsylvania Station.',
            image_url='https://www.hollywoodreporter.com/wp-content/uploads/2021/03/GettyImages-1286738801_EA-H-2021-1617146947.jpg?w=1296'
        ),
        Landmarks(
            name='The Apollo Theater',
            description='A music hall located at 253 West 125th Street between Adam Clayton Powell Jr. Boulevard (Seventh Avenue) and Frederick Douglass Boulevard',
            image_url='https://images.ctfassets.net/1aemqu6a6t65/60AksK8fMux0IYzka9ypIL/5304b87d646d4f6f32346e0423e301a2/theapollo_kateglicksberg-0105?w=1200&h=800&q=75'
        ),
        Landmarks(
            name='The Cloisters',
            description='A museum in Fort Tryon Park in Washington Heights, Manhattan, New York City, specializing in European medieval architecture, sculpture, and decorative arts.',
            image_url='https://cdn.sanity.io/images/cctd4ker/production/13a51854d783d89f19d359680c27ade2331b3272-3840x2160.jpg?w=3840&q=75&fit=clip&auto=format'
        ),
        Landmarks(
            name='Citi Field',
            description='A baseball park located in Flushing Meadows–Corona Park in the New York City borough of Queens. Completed in 2009, it is the home field of the New York Mets of Major League Baseball.',
            image_url='https://populous.com/wp-content/uploads/2018/01/POP_05_2647_00_N197_medium.jpg'
        )

    ]
    db.session.add_all(landmarks)
    db.session.commit()
    print('Database seeded!')
    
if __name__ == '__main__':
  
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!
