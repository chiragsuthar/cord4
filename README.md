# Chatting System

Chatting System is a Django-based web application developed to provide a platform for users to communicate through messages, with additional features such as user authentication, profile management, message scheduling, event-based messaging, and more.

## Features

- **User Authentication**: Users can register, log in, and log out. Login is based on phone number and OTP verification.
- **Profile Management**: Users can edit their profile, including updating their name and profile picture.
- **Chat Functionality**: Users can send, receive, forward, and reply to messages and media.
- **Suggested Replies**: Users are provided with suggested replies based on the last sent message.
- **Message Scheduling**: Users can schedule messages to be sent at a later time.
- **Event-Based Auto-Sending Messages**: Messages can be automatically sent for specific events, such as Diwali greetings or birthday celebrations.
- **Recurring Messages**: Users can schedule recurring messages.
- **Settings**: Users can toggle auto-sending and recurring message features on or off, and can also send messages to selected users.

## Installation

1. **Clone the repository:**

2. **Navigate into the project directory:**

3. **Create and activate a virtual environment:**

4. **Install the required packages:**

5. **Set up your database:**
- Make sure you have MongoDB installed and running.

6. **Apply migrations:**

7. **Create a superuser (for admin access):**

8. **Run the development server:**

9. **Access the application at** `http://localhost:8000`.

## API Endpoints

- **User Profile**: `/api/profile/`
- **Verify Phone Number**: `/api/verify-phone/`
- **Verify OTP**: `/api/verify-otp/`
- **Update Profile**: `/api/update-profile/`
- **Send Message**: `/api/send-message/`
- **Get Messages**: `/api/get-messages/`
- **Schedule Message**: `/api/schedule-message/`
- **Send Auto Messages**: `/api/send-auto-messages/`
- **Schedule Recurring Message**: `/api/schedule-recurring-message/`
- **Update Settings**: `/api/update-settings/`

## Technologies Used

- Django
- Django Rest Framework
- MongoDB
- Twilio (for OTP verification)

## Contributors

- [Chirag Suthar](https://github.com/chiragsuthar)
