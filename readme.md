# Namma Krishi IVR System

A Django-based Interactive Voice Response (IVR) system for agricultural machine rental services. This system allows farmers to call and rent agricultural equipment through a voice-guided menu system powered by Twilio.

## What it does

This IVR system helps farmers easily rent agricultural machines by calling a phone number. The system guides them through different options to:

- Find agricultural equipment providers in their locality
- Connect with lessors for tractors and farming vehicles
- Get information about attachments and other farming equipment
- Connect directly to service providers

## Features

- **Multi-level menu system** - Easy navigation through voice prompts
- **Location-based services** - Find providers in Bangalore, Mysuru, and Gadag
- **Call logging** - Tracks all calls for analytics and follow-up
- **Direct connection** - Connects callers directly to service providers
- **Timeout handling** - Graceful handling of user inactivity

## Tech Stack

- **Django 5.2.3** - Web framework
- **Twilio Voice API** - IVR functionality
- **SQLite** - Database for call logging
- **Python 3.12** - Programming language

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/namma-krishi-ivr.git
cd namma-krishi-ivr
```

2. Install dependencies:
```bash
pip install django twilio
```

3. Run migrations:
```bash
python manage.py migrate
```

4. Start the development server:
```bash
python manage.py runserver
```

## Twilio Setup

1. Create a Twilio account and get your phone number
2. Set up a webhook URL pointing to your Django application
3. Configure the webhook to point to `/` for incoming calls

For development, you can use ngrok to expose your local server:
```bash
ngrok http 8000
```

Then set your Twilio webhook URL to: `https://your-ngrok-url.ngrok.io/`

To download ngrok, refer this link : `https://dashboard.ngrok.com/get-started/setup/linux`

## Call Flow

```
Welcome Message
├── Press 1: Rent a machine
│   └── Select Locality
│       └── Press 1: Bangalore
│           └── Select Provider
│               └── Press 1: Suntec Agrimart
│                   └── Select Equipment Type
│                       ├── Press 1: Farming Vehicles → Connect to Provider
│                       └── Press 2: Attachments → Connect to Provider
├── Press 2: Current rental details (Under development)
└── Press 3: Customer support (Under development)
```

## Database Schema

The system uses a simple `CallLog` model to track calls:

- `call_sid` - Unique Twilio call identifier
- `from_number` - Caller's phone number
- `to_number` - Called number
- `status` - Call status
- `duration` - Call duration
- `direction` - Call direction (inbound/outbound)
- `created_at` - Timestamp

## Project Structure

```
├── manage.py
├── db.sqlite3
├── NAMMA_KRISHI_IVR/          # Main Django project
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── ivr/                       # IVR app
    ├── models.py              # CallLog model
    ├── views.py               # IVR logic
    ├── urls.py                # URL routing
    └── migrations/
```

## Configuration

Make sure to update the following in production:

- Set `DEBUG = False` in settings.py
- Add your domain to `ALLOWED_HOSTS`
- Update the phone number in `connect_farming_vehicle()` and `connect_attachments()` functions
- Configure proper database (PostgreSQL recommended for production)

## Contributing

Feel free to submit issues and pull requests. Areas that need improvement:

- Add more locations and providers
- Implement features for options 2 and 3
- Add proper error handling and logging
- Implement call recording functionality
- Add admin interface for managing providers

## License

This project is open source and available under the MIT License.

## Contact

For questions or support, please open an issue on GitHub.