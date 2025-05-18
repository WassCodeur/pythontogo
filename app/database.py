from datetime import datetime, timezone, timedelta

import random
import json

hero_images = [
    "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744070856/hero_iapsxz.jpg",
    "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744070811/groupe_picture_accra_rudcom.jpg",
    "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744070808/pycon_lezpmd.jpg",
    "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744070949/WUL_0456_qerwtk.jpg",
]

events_data = [
    {
        "id": 3,
        "title": "PyCon Togo 2025",
        "description": "The first Python Conference in Togo bringing together developers, enthusiasts, and experts from across Togo and beyond.",
        "short_description": "The biggest Python conference in Togo. Three days of talks, workshops, and networking.",
        "category": "Conference",
        "date": "23 August 2025",
        "start_date": "23 August 2025 07:00 GMT",
        "end_date": "23 August 2025 18:00 GMT",
        "time": "All day",
        "location": "Coming Soon",
        "venue_address": "Coming Soon",
        "image_url": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1747588996/Group_6_r7n6id.png",
        "website": "https://pycontg.pytogo.org",
        "registration_link": "https://pycontg.pytogo.org/register",
        "status": "ongoing",
        "speakers": [],
        "schedule": [],
    },
    {
        "id": 4,
        "title": "Join the Python Togo Community",
        "description": "Join the Python Togo community and connect with other Python enthusiasts. Whether you're a beginner or an experienced developer, there's a place for you in our community.",
        "short_description": "Join the Python Togo community and connect with other Python enthusiasts.",
        "category": "Community",
        "date": datetime.now(timezone.utc).strftime("%d %B %Y"),
        "start_date": datetime.now(timezone.utc).strftime("%d %B %Y %H:%M %Z"),
        "end_date": (
            (datetime.now(timezone.utc) + timedelta(days=1)).strftime(
                "%d %B %Y %H:%M %Z"
            )
        ),
        "time": datetime.now(timezone.utc).strftime("%H:%M %Z"),
        "location": "Discord",
        "venue_address": "Discord",
        "image_url": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1747591135/Copie_de_Python_Togp.ai_1_z1ikuj.png",
        "status": "upcoming",
        "website": "https://pytogo.org/discord",
        "registration_link": "https://pytogo.org/discord",
        "speakers": [],
        "schedule": [],
    },
    {
        "id": 5,
        "title": "Information Session on Python Togo",
        "description": "Join us for an information session on Python Togo. Learn about our mission, vision, and how you can get involved.",
        "short_description": "Join us for an information session on Python Togo. Learn about our mission, vision, and how you can get involved.",
        "category": "Community",
        "date": "17 May 2025",
        "start_date": "17 May 2025 09:00 GMT",
        "end_date": "17 May 2025 10:00  GMT",
        "time": "1 Hour",
        "location": "Discord",
        "venue_address": "Discord",
        "image_url": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1747589635/PythonTG.psd_cyxglb.png",
        "status": "upcoming",
        "website": "https://pytogo.org/discord",
        "registration_link": "https://pytogo.org/discord",
        "speakers": [],
        "schedule": [],
    },
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
        "image_url": "https://res.cloudinary.com/dvg7vky5o/image/upload/pyday_x0goz4.jpg",
        "website": "https://lu.ma/runpiv8k",
        "registration_link": "https://lu.ma/runpiv8k",
        "status": "past",
    },
    {
        "id": 2,
        "title": "PyCon Africa Extended Togo 2024",
        "description": "The PyCon Africa Exitended Togo is a full-day event that serve as feedback session for the PyCon Africa 2024 conference. It is an opportunity for attendees to share their experiences, insights, and learnings from the conference.",
        "short_description": "The PyCon Africa Exitended Togo is a full-day event that serve as feedback session for the PyCon Africa 2024 conference.",
        "category": "Conference",
        "date": "30 November 2024",
        "start_date": "30 November 2024 09:00 GMT",
        "end_date": "30 November 2024 17:00 GMT",
        "time": "All day",
        "location": "Institute Polytechnic Defitech",
        "venue_address": "Sito-Aéroport, Lomé, Togo",
        "image_url": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1747589776/pyday_togo_owvze6.jpg",
        "status": "past",
        "website": "https://lu.ma/runpiv8k",
        "registration_link": "https://lu.ma/runpiv8k",
        "speakers": [],
        "schedule": [],
    },
    # trip to pycon africa at Accra
    {
        "id": 0,
        "title": "Trip to PyCon Africa 2024",
        "description": "Our Team is going to PyCon Africa 2024 in Accra, Ghana. Join us for a trip to the conference and meet other Python enthusiasts.",
        "short_description": "Join us for a trip to PyCon Africa 2024 in Accra, Ghana.",
        "category": "Trip",
        "date": "23 September 2024",
        "start_date": "24 September 2024 09:00 GMT",
        "end_date": "28 September 2024 17:00 GMT",
        "time": "1 week",
        "location": "Accra, Ghana",
        "venue_address": "Accra, Cedi Conference Center",
        "image_url": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744070811/groupe_picture_accra_rudcom.jpg",
        "website": "https://pycontg.pytogo.org",
        "registration_link": "https://pycontg.pytogo.org",
        "status": "past",
    },
]


teams_members = [
    {
        "name": "Wachiou BOURAIMA",
        "role": "President | Co-founder",
        "image": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744072317/wass_lejeso.jpg",
    },
    {
        "name": "Agnilonda PAKOU",
        "role": "Vice-President | co-founder",
        "image": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744072312/pakou_rks87v.jpg",
    },
    {
        "name": " Geoffrey LOGOVI",
        "role": "Executive Director | co-founder",
        "image": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744072313/geoffrey_bfcnl4.png",
    },
    {
        "name": "Parfait TOKE",
        "role": "General Councillor | co-founder",
        "image": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744072320/parfait_gvjg7z.jpg",
    },
    {
        "name": "Laboré kodjo AGBETSIASSI",
        "role": "Education, Training and Mentoring Managers | co-founder",
        "image": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744072336/labore_bamkph.jpg",
    },
    {
        "name": "Samadou OURO-AGOROUKO",
        "role": "Education, Training and Mentoring Managers | co-founder",
        "image": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744072312/samadou_hpu656.jpg",
    },
    {
        "name": "Irène AMEDJI",
        "role": "Head of Communications and Design | Co-founder",
        "image": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744072311/irene_avrtzw.jpg",
    },
    {
        "name": "Yves HOUANGASSI",
        "role": "Head of Communications and Design | Co-founder",
        "image": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744072323/yves_m5ijgw.png",
    },
    {
        "name": "Samira AMADOU",
        "role": "Partnerships and External Relations Advisor | Co-founder",
        "image": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744072314/samira_x3b53b.jpg",
    },
    {
        "name": "Emmanuel AMELA",
        "role": "Deputy Secretary | Co-founder",
        "image": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744072309/emmanuel_fgzpks.jpg",
    },
    {
        "name": "Medede BIDASSA",
        "role": "Treasurer | co-founder",
        "image": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744072309/happy_fqkpto.jpg",
    },
    {
        "name": "Waficah OLOSSOUMARE",
        "role": "Deputy Treasurer | Co-founder",
        "image": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744072333/waficah2_iebump.jpg",
    },
    {
        "name": "Akinwumi OGUNDIPE",
        "role": "Product Designer | Core Contributor",
        "image": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744072311/akinwumi_nei6fq.jpg",
    },
]

galleries = [
    {
        "url": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744070809/pyconafrica20241_syencp.jpg",
        "caption": "Community networking session",
        "height": random.randrange(30, 60),
    },
    {
        "url": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744070809/pyconafrica20242_qg88cd.jpg",
        "caption": "PyCon Africa 2024 Team",
        "height": random.randrange(30, 60),
    },
    {
        "url": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744070815/pyconafrica20243_dtrdhr.jpg",
        "caption": "Python workshop for beginners",
        "height": random.randrange(30, 60),
    },
    {
        "url": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744070870/WUL_0426_md0krb.jpg",
        "caption": "Keynote presentation",
        "height": random.randrange(30, 60),
    },
    {
        "url": "WUL_0338.jpg",
        "caption": "Networking during coffee break",
        "height": random.randrange(30, 60),
    },
    {
        "url": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744070811/groupe_picture_accra_rudcom.jpg",
        "caption": "Hackathon winning team",
        "height": random.randrange(30, 60),
    },
    {
        "url": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744070949/WUL_0456_qerwtk.jpg",
        "caption": "Conference venue entrance",
        "height": random.randrange(30, 60),
    },
    {
        "url": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744070862/WUL_0433_1_wuak8r.jpg",
        "caption": "Keynote presentation",
        "height": random.randrange(30, 60),
    },
    {
        "url": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744070878/WUL_0433_vdmj2j.jpg",
        "caption": "Keynote presentation",
        "height": random.randrange(30, 60),
    },
    {
        "url": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744070808/pycon_lezpmd.jpg",
        "caption": "PyConAfrica",
        "height": random.randrange(30, 60),
    },
    {
        "url": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744070948/WUL_0468_1_pdlydh.jpg",
        "caption": "PyDay Togo 2024",
        "height": random.randrange(30, 60),
    },
    {
        "url": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744070841/WUL_0317_vyezwq.jpg",
        "caption": "Keynote presentation",
        "height": random.randrange(30, 60),
    },
    {
        "url": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744070843/WUL_0393_arlbnx.jpg",
        "caption": "Keynote presentation",
        "height": random.randrange(30, 60),
    },
    {
        "url": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744070975/WUL_0481_krzjew.jpg",
        "caption": "Networking during coffee break",
        "height": random.randrange(30, 60),
    },
    {
        "url": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744070824/WUL_0390_uaf6ac.jpg",
        "caption": "Keynote presentation",
        "height": random.randrange(30, 60),
    },
    {
        "url": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744070968/WUL_0468_bcodxc.jpg",
        "caption": "Python in Africa",
        "height": random.randrange(30, 60),
    },
    {
        "url": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744070872/WUL_0434_b7vxhx.jpg",
        "caption": "Keynote presentation",
        "height": random.randrange(30, 60),
    },
    {
        "url": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744070913/WUL_0440_m1kzzu.jpg",
        "caption": "Keynote presentation",
        "height": random.randrange(30, 60),
    },
    {
        "url": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744070954/WUL_0469_spgjme.jpg",
        "caption": "attendees networking",
        "height": random.randrange(30, 60),
    },
    {
        "url": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744070900/WUL_0437_1_wmcpun.jpg",
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


