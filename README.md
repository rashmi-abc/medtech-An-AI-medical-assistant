# MeDTech

## Overview
MeDTech is an AI-driven Telemedicine platform designed to improve healthcare accessibility in rural areas. It provides advanced features such as AI-powered skin disease detection, symptom-based diagnosis, prescription analysis, and a blood request and donation system. The platform can be deployed in a kiosk, used as a website, or accessed via a mobile app.

## Features

### AI-Powered Skin Disease Detection
- Analyzes uploaded skin images to detect diseases.
- Provides remedies, treatments, and preventive measures.

### Symptom-Based Diagnosis and Doctor Recommendations
- Diagnoses diseases based on user-provided symptoms.
- Suggests preventive measures and recommends suitable doctors for consultation.

### Prescription Analyzer
- Extracts medication details from uploaded prescriptions.
- Identifies drug names, dosages, instructions, and potential side effects.

### Blood Request, Donation, and Prescription Manager
- Facilitates blood requests and donations to help patients in need.
- Manages prescriptions and doctor appointments to improve healthcare accessibility.

## Deployment
MeDTech can be deployed in multiple formats:
- **Kiosk**: Installed in rural healthcare centers for easy access.
- **Website**: Accessible from any device with an internet connection.
- **Mobile App**: Allows users to access healthcare services on the go.

## Technologies Used
- **Backend**: Python
- **Frontend**: Streamlit
- **AI Model**: Custom-trained skin disease detection model (Roboflow)
- **Cloud Services**: Firebase
- **Communication**: Twilio API for SMS notifications

## Installation & Setup
### Prerequisites
Ensure you have the following installed:
- Streamlit
- Flutter(For app)
- Python (for AI model integration)

### Clone the Repository
```bash
 git clone https://github.com/your-username/MeDTech.git
 cd MeDTech
```

## API Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/diagnose` | POST | Diagnose disease based on symptoms |
| `/api/skin-detect` | POST | Analyze skin disease from image |
| `/api/prescription-analyze` | POST | Extract details from prescription |
| `/api/blood-request` | POST | Request for blood donation |
| `/api/doctors` | GET | Fetch recommended doctors |

## Contribution
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`feature-branch`).
3. Commit your changes.
4. Push to your fork and submit a Pull Request.



