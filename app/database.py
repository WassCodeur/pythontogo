from datetime import datetime, timezone, timedelta

import random
import json

events_data = [
    {
        "id": 1,
        "title": "PyDay Togo 2024",
        "description": """Learn how to use Python for data analysis and visualization in this full-day workshop. This
            workshop is perfect for beginners who want to get started with data science using Python.
            
            Topics covered include:
            - Introduction to Python for data analysis
            - Data manipulation with pandas
            - Numerical computing with numpy
            - Data visualization with matplotlib and seaborn
            - Introduction to machine learning with scikit-learn
            
            Participants should bring their own laptops with Python installed. We will provide
            instructions for setting up your environment before the workshop.""",
        "short_description": "Learn how to use Python for data analysis and visualization. This workshop covers pandas, numpy, and matplotlib.",
        "category": "Conference",
        "date": "30 November 2024",
        "start_date": "30 November 2024 09:00 GMT",
        "end_date": "30 November 2024 17:00 GMT",
        "time": "09:00 - 17:00",
        "location": "Institute Polytechnic Defitech",
        "venue_address": "Sito-Aéroport, Lomé, Togo",
        "image_url": "/static/images/events/pyday.jpeg",
        "status": "upcoming",
        "speakers": [
            {
                "name": "Dr. Kodjo Adade",
                "title": "Data Scientist, University of Lomé",
                "image_url": "/static/images/speakers/kodjo_adade.jpg",
            },
            {
                "name": "Ama Sika",
                "title": "Python Developer, Tech Togo",
                "image_url": "/static/images/speakers/ama_sika.jpg",
            },
            {
                "name": "Pascal Mensah",
                "title": "ML Engineer, AI Africa",
                "image_url": "/static/images/speakers/pascal_mensah.jpg",
            },
        ],
        "schedule": [
            {
                "time": "09:00 - 09:30",
                "title": "Registration and Setup",
                "description": "Get set up with the workshop environment and materials",
            },
            {
                "time": "09:30 - 11:00",
                "title": "Introduction to Python for Data Science",
                "description": "Overview of Python and its data science ecosystem",
            },
            {
                "time": "11:00 - 12:30",
                "title": "Data Manipulation with Pandas",
                "description": "Learn how to load, clean, and transform data",
            },
            {"time": "12:30 - 13:30", "title": "Lunch Break", "description": ""},
            {
                "time": "13:30 - 15:00",
                "title": "Data Visualization",
                "description": "Creating effective visualizations with matplotlib and seaborn",
            },
            {
                "time": "15:00 - 16:30",
                "title": "Introduction to Machine Learning",
                "description": "Basic ML concepts and implementing simple models with scikit-learn",
            },
            {
                "time": "16:30 - 17:00",
                "title": "Q&A and Wrap-up",
                "description": "Final questions and next steps",
            },
        ],
    },
    {
        "id": 2,
        "title": "PyCon Togo 2024",
        "description": "The biggest Python conference in Togo. Three days of talks, workshops, and networking with Python enthusiasts from across West Africa.",
        "short_description": "The biggest Python conference in Togo. Three days of talks, workshops, and networking.",
        "category": "Conference",
        "date": "Coming Soon",
        "start_date": "30 November 2024 09:00 GMT",
        "end_date": "30 November 2024 17:00 GMT",
        "time": "All day",
        "location": "Institute Polytechnic Defitech",
        "venue_address": "Sito-Aéroport, Lomé, Togo",
        "image_url": "/static/images/events/pyday_togo.JPG",
        "status": "ongoing",
        "speakers": [],
        "schedule": [],
    },
    {
        "id": 3,
        "title": "PyCon Togo 2025",
        "description": "The biggest Python conference in Togo. Three days of talks, workshops, and networking with Python enthusiasts from across West Africa.",
        "short_description": "The biggest Python conference in Togo. Three days of talks, workshops, and networking.",
        "category": "Conference",
        "date": "Coming Soon",
        "start_date": "30 November 2025 09:00 GMT",
        "end_date": "30 November 2025 17:00 GMT",
        "time": "All day",
        "location": "Coming Soon",
        "venue_address": "Coming Soon",
        "image_url": "/static/images/events/pyday_togo.JPG",
        "status": "ongoing",
        "speakers": [],
        "schedule": [],
    },
    {
        "id": 3,
        "title": "Django Web Development",
        "description": "Learn how to build web applications using Django, the Python web framework for perfectionists with deadlines.",
        "short_description": "Learn how to build web applications using Django, the Python web framework.",
        "category": "Meetup",
        "date": "15 April 2025",
        "start_date": "15 April 2025 18:00 GMT",
        "end_date": "15 April 2025 20:00 GMT",
        "time": "18:00 - 20:00",
        "location": "Coming Soon",
        "venue_address": "45 Rue des Entrepreneurs, Lomé",
        "image_url": "/static/images/events/django_meetup.webp",
        "status": "upcoming",
        "speakers": [],
        "schedule": [],
    },
    {
        "id": 4,
        "title": "What is Python and Why Should You Learn It?",
        "description": "What is Python and why should you learn it? In this workshop, we'll cover the basics of Python and how it can be used for data analysis, web development, and more.",
        "short_description": "What is Python and why should you learn it? In this workshop, we'll cover the basics of Python.",
        "category": "Blog",
        "date": datetime.now(timezone.utc).strftime("%d %B %Y"),
        "start_date": datetime.now(timezone.utc).strftime("%d %B %Y %H:%M %Z"),
        "end_date": (
            (datetime.now(timezone.utc) + timedelta(days=1)).strftime(
                "%d %B %Y %H:%M %Z"
            )
        ),
        "time": datetime.now(timezone.utc).strftime("%H:%M %Z"),
        "location": "Coming Soon",
        "venue_address": "45 Rue des Entrepreneurs, Lomé",
        "image_url": "/static/images/events/What-is-Python.jpg",
        "status": "upcoming",
        "speakers": [],
        "schedule": [],
    },
]


teams_members = [
    {
        "name": "Wachiou BOURAIMA",
        "role": "President | Co-founder",
        "image": "wass.jpeg",
    },
    {
        "name": "Agnilonda PAKOU",
        "role": "Vice-President | co-founder",
        "image": "pakou.jpg",
    },
    {
        "name": " Geoffrey LOGOVI",
        "role": "Executive Director | co-founder",
        "image": "geoffrey.png",
    },
    {
        "name": "Parfait TOKE",
        "role": "General Councillor | co-founder",
        "image": "parfait.jpg",
    },
    {
        "name": "Laboré kodjo AGBETSIASSI",
        "role": "Education, Training and Mentoring Managers | co-founder",
        "image": "labore.JPG",
    },
    {
        "name": "Samadou OURO-AGOROUKO",
        "role": "Education, Training and Mentoring Managers | co-founder",
        "image": "samadou.jpeg",
    },
    {
        "name": "Irène AMEDJI",
        "role": "Head of Communications and Design | Co-founder",
        "image": "irene.jpeg",
    },
    {
        "name": "Yves HOUANGASSI",
        "role": "Head of Communications and Design | Co-founder",
        "image": "yves.png",
    },
    {
        "name": "Samira AMADOU",
        "role": "Partnerships and External Relations Advisor | Co-founder",
        "image": "samira.jpeg",
    },
    {
        "name": "Emmanuel AMELA",
        "role": "Deputy Secretary | Co-founder",
        "image": "emmanuel.jpeg",
    },
    {
        "name": "Medede BIDASSA",
        "role": "Treasurer | co-founder",
        "image": "happy.jpeg",
    },
    {
        "name": "Waficah OLOSSOUMARE",
        "role": "Deputy Treasurer | Co-founder",
        "image": "waficah2.jpeg",
    },
    {
        "name": "Akinwumi OGUNDIPE",
        "role": "Product Designer | Core Contributor",
        "image": "akinwumi.JPG",
    },
]

galleries = [
    {
        "url": "pyconafrica20241.jpeg",
        "caption": "Community networking session",
        "height": random.randrange(30, 60),
    },
    {
        "url": "pyconafrica20242.jpeg",
        "caption": "PyCon Africa 2024 Team",
        "height": random.randrange(30, 60),
    },
    {
        "url": "pyconafrica20243.jpeg",
        "caption": "Python workshop for beginners",
        "height": random.randrange(30, 60),
    },
    {
        "url": "WUL_0426.jpg",
        "caption": "Keynote presentation",
        "height": random.randrange(30, 60),
    },
    {
        "url": "WUL_0338.jpg",
        "caption": "Networking during coffee break",
        "height": random.randrange(30, 60),
    },
    {
        "url": "groupe_picture_accra.jpeg",
        "caption": "Hackathon winning team",
        "height": random.randrange(30, 60),
    },
    {
        "url": "WUL_0456.jpg",
        "caption": "Conference venue entrance",
        "height": random.randrange(30, 60),
    },
    {
        "url": "WUL_0433 (1).jpg",
        "caption": "Keynote presentation",
        "height": random.randrange(30, 60),
    },
    {
        "url": "pycon.jpeg",
        "caption": "PyConAfrica",
        "height": random.randrange(30, 60),
    },
    {
        "url": "WUL_0468(1).jpg",
        "caption": "PyDay Togo 2024",
        "height": random.randrange(30, 60),
    },
    {
        "url": "WUL_0317.jpg",
        "caption": "Keynote presentation",
        "height": random.randrange(30, 60),
    },
    {
        "url": "WUL_0393.jpg",
        "caption": "Keynote presentation",
        "height": random.randrange(30, 60),
    },
    {
        "url": "WUL_0481.jpg",
        "caption": "Networking during coffee break",
        "height": random.randrange(30, 60),
    },
    {
        "url": "WUL_0390.jpg",
        "caption": "Keynote presentation",
        "height": random.randrange(30, 60),
    },
    {
        "url": "WUL_0468.jpg",
        "caption": "Python in Africa",
        "height": random.randrange(30, 60),
    },
    {
        "url": "WUL_0434.jpg",
        "caption": "Keynote presentation",
        "height": random.randrange(30, 60),
    },
    {
        "url": "WUL_0440.jpg",
        "caption": "Keynote presentation",
        "height": random.randrange(30, 60),
    },
    {
        "url": "WUL_0469.jpg",
        "caption": "attendees networking",
        "height": random.randrange(30, 60),
    },
    {
        "url": "WUL_0437(1).jpg",
        "caption": "attendee questions",
        "height": random.randrange(30, 60),
    },
]

parteners = [
    {
        "name": "Python Software Foundation",
        "logo_url": "psf-logo.png",
        "symbol": "PSF",
    },
    {
        "name": "Python Ghana",
        "logo_url": "pyghana.png",
        "symbol": "pyghana-logo",
    },
    {"name": "Hyever", "logo_url": "hyver.png", "symbol": "hyver-logo"},
    {
        "name": "Tech Communities Day",
        "logo_url": "tcd.png",
        "symbol": "tcd-logo",
    },
    {
        "name": "Amazing Girls In Tech",
        "logo_url": "amz_girls.png",
        "symbol": "amz_girls-logo",
    },
    {
        "name": "TEDx VITChennai",
        "logo_url": "tedx.png",
        "symbol": "tcd-logo",
    },
    {
        "name": "Africa Blockchain Community",
        "logo_url": "abc-logo-full.png",
        "symbol": "abc-logo",
    },
    # {
    #     "name": "Python Software Foundation",
    #     "logo_url": "tedx.png",
    #     "symbol": "TEDX",
    # },
]

# [{"url": "", "caption": "", "data-height": random.randrange(30, 60)}]
swags = [
    {
        "name": "Python Togo T-Shirt",
        "description": "Proudly represent the Python Togo community with our official t-shirt. Made from high-quality cotton.",
        "price": 3500,
        "originalPrice": 5000,
        "images": [
            "/static/images/swags/tshirt.png",
        ],
    },
    {
        "name": "Python Togo Travel Mugs & Tumblers",
        "description": "This tumbler boasts a large capacity and an ergonomic handle for a comfortable hold.",
        "price": 2500,
        "originalPrice": 5000,
        "images": [
            "/static/images/swags/thunder.png",
            "/static/images/swags/bootle.png",
        ],
    },
    {
        "name": "Python Togo Hoodie",
        "description": "Stay warm with our Python Togo hoodie. Perfect for coding nights and meetups.",
        "price": 7500,
        "originalPrice": 9000,
        "images": [
            "/static/images/swags/hoodie.png",
        ],
    },
    {
        "name": "Python Togo Cap",
        "description": "Complete your tech look with our exclusive Python Togo cap. Adjustable and comfortable.",
        "price": 2500,
        "originalPrice": 3500,
        "images": [
            "/static/images/swags/cap.png",
        ],
    },
    {
        "name": "Python Togo Stickers",
        "description": "Decorate your laptop, phone, and more with our Python Togo stickers. Durable and waterproof.",
        "price": 500,
        "originalPrice": 1000,
        "images": [
            "/static/images/favicon.png",
            "/static/images/logo.png",
        ],
    },
]


def get_all_events():
    now = datetime.now(timezone.utc)

    for event in events_data:
        date_obj = datetime.strptime(event["start_date"], "%d %B %Y %H:%M %Z")
        end_date_obj = datetime.strptime(event["end_date"], "%d %B %Y %H:%M %Z")

        start_date = date_obj.replace(tzinfo=timezone.utc)
        end_date = end_date_obj.replace(tzinfo=timezone.utc)
        if start_date > now:
            event["status"] = "upcoming"
        elif start_date < now and end_date < now:
            event["status"] = "past"
        else:
            event["status"] = "ongoing"

    return events_data


def get_events_by_status(status):
    return [event for event in events_data if event["status"] == status]


def get_event_by_id(event_id):
    for event in events_data:
        if event["id"] == event_id:
            return event
    return None


def get_teams_members():
    return teams_members


def get_swags():
    return swags


def get_parteners():
    return parteners
