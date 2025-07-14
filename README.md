# Medula0 Django Web Application

This project replicates sections of the Medula Eczane application used in Turkey. It includes modules for:
- Raporlar (Reports)
- Hastalık Öyküleri (Medical Histories)
- Eskiden Alınmış Reçeteler (Previous Prescriptions)
- En Sonki Reçete (Latest Prescription)
- Kişisel Bilgiler (Personal Information)

## Setup Instructions

1. **Create a virtual environment** (already set up in `.venv`).
2. **Install dependencies:**
   ```zsh
   source .venv/bin/activate
   pip install django
   ```
3. **Run migrations:**
   ```zsh
   python manage.py migrate
   ```
4. **Start the development server:**
   ```zsh
   python manage.py runserver
   ```

## Project Structure
- `core/` - Main app for business logic and models
- `medula0/` - Project settings

## Next Steps
- Add models for profiles, prescriptions, medical histories, and reports
- Populate with sample data
- Build basic views and templates
