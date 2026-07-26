# Aviator Statistics Analyzer

## 🎯 Plateforme d'Analyse Statistique Professionnelle du Jeu Aviator

Une application web complète pour collecter, analyser et visualiser les multiplicateurs du jeu Aviator avec des statistiques avancées, détection d'anomalies et estimations probabilistes basées sur les données historiques.

### ⚠️ Avertissement Important

**Cette application ne prétend JAMAIS connaître ou prédire avec certitude le prochain multiplicateur.**

Toutes les analyses sont présentées comme :
- Probabilités observées
- Tendances historiques
- Estimations statistiques
- Fréquences empiriques

Les résultats ne garantissent pas les résultats futurs.

---

## 🚀 Fonctionnalités Principales

### 📊 Collecte et Stockage
- ✅ Importation de données (CSV, Excel, JSON)
- ✅ Saisie manuelle
- ✅ API d'intégration (futures sources temps réel)
- ✅ Nettoyage automatique des données
- ✅ Validation et journal des erreurs

### 📈 Statistiques Avancées
- ✅ Calculs automatiques (moyenne, médiane, écart-type, variance, quartiles, déciles)
- ✅ Distributions de probabilités empiriques
- ✅ Analyse par plages (1.20, 2-5, 5-10, 10-20, 20-50, 50-100, 100+)
- ✅ Tests statistiques (KS, Chi², Autocorrélation)
- ✅ Détection de skewness et kurtosis

### 🔍 Détection de Tendances et Anomalies
- ✅ Détection de séries (petits/gros multiplicateurs)
- ✅ Alternances et patterns
- ✅ Absence prolongée de seuils (10x, 50x, 100x)
- ✅ Z-score et anomalies statistiques
- ✅ Alertes configurables

### 🪟 Fenêtres Glissantes
- ✅ Analyse sur 10, 20, 50, 100, 500, 1000 tours
- ✅ Calcul dynamique des statistiques
- ✅ Comparaison avec historique

### 📅 Analyse Temporelle
- ✅ Agrégation par minute, heure, jour, semaine, mois
- ✅ Évolutions temporelles
- ✅ Tendances saisonnières

### 🤖 Module IA/ML
- ✅ Random Forest
- ✅ Gradient Boosting
- ✅ XGBoost (optionnel)
- ✅ LSTM (optionnel)
- ✅ Feature Engineering automatique

**Objectif** : Estimer les probabilités de plages de multiplicateurs (non prédire le suivant)

### 📊 Visualisations
- ✅ Histogrammes
- ✅ Courbes (timeseries)
- ✅ Heatmaps
- ✅ Box plots
- ✅ Scatter plots
- ✅ Radar charts
- ✅ Pie charts
- ✅ Dashboard temps réel (WebSocket)

### 👥 Authentification et Permissions
- ✅ JWT Authentication
- ✅ Rôles : Admin, Analyste, Utilisateur
- ✅ Journalisation complète des connexions
- ✅ Historique des actions

### 📤 Exports
- ✅ PDF
- ✅ Excel
- ✅ CSV
- ✅ JSON

---

## 🏗️ Architecture

### Backend
- **Framework**: Django 5 + Django REST Framework
- **Base de données**: PostgreSQL
- **Cache**: Redis
- **Async**: Celery + Channels (WebSocket)
- **Science des données**: Pandas, NumPy, SciPy, Scikit-learn, XGBoost

### Frontend
- **Framework**: React + TypeScript
- **Graphiques**: Chart.js / ECharts / Plotly
- **Real-time**: WebSocket via Channels
- **UI**: Responsive, Mode clair/sombre

### Infrastructure
- **Conteneurisation**: Docker + Docker Compose
- **Serveur Web**: Nginx
- **WSGI**: Gunicorn
- **CI/CD**: GitHub Actions

---

## 📁 Structure du Projet

```
aviator-stats-analyzer/
├── backend/
│   ├── config/                    # Django settings
│   ├── apps/
│   │   ├── rounds/               # Modèles et logique des tours
│   │   ├── analytics/            # Statistiques et analyses
│   │   ├── predictions/          # Modèles ML et prédictions
│   │   ├── alerts/               # Système d'alertes
│   │   ├── users/                # Authentification et permissions
│   │   └── data_import/          # Import de données
│   ├── core/                      # Utilities et décorateurs
│   ├── api/                       # Endpoints REST
│   ├── management/                # Commandes Django
│   ├── requirements.txt
│   ├── manage.py
│   └── wsgi.py
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── hooks/
│   │   ├── services/
│   │   └── styles/
│   ├── public/
│   └── package.json
├── docker-compose.yml
├── Dockerfile
├── .github/
│   └── workflows/                # GitHub Actions
├── docs/                          # Documentation
├── tests/
└── README.md
```

---

## 🔧 Installation Rapide

### Prérequis
- Python 3.11+
- Node.js 18+
- Docker & Docker Compose
- PostgreSQL 15+

### 1. Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # ou `venv\Scripts\activate` sur Windows
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### 2. Frontend Setup

```bash
cd frontend
npm install
npm start
```

### 3. Avec Docker Compose

```bash
docker-compose up -d
```

---

## 📚 Documentation

- [Backend Setup](./docs/BACKEND_SETUP.md)
- [Frontend Setup](./docs/FRONTEND_SETUP.md)
- [Architecture](./docs/ARCHITECTURE.md)
- [API Documentation](./docs/API.md)
- [Database Schema](./docs/DATABASE.md)
- [Deployment Guide](./docs/DEPLOYMENT.md)

---

## 🧪 Tests

```bash
# Tests unitaires
pytest backend/tests/

# Tests API
pytest backend/tests/api/

# Coverage
pytest --cov=backend backend/tests/
```

---

## 🔐 Sécurité

- ✅ JWT Authentication
- ✅ Protection CSRF
- ✅ Protection XSS
- ✅ Protection SQL Injection (Django ORM)
- ✅ Validation des données
- ✅ Rate limiting
- ✅ Journalisation complète

---

## 📈 Performance

- ✅ Cache Redis
- ✅ Celery pour les tâches asynchrones
- ✅ Pagination
- ✅ Optimisation SQL (select_related, prefetch_related)
- ✅ Index PostgreSQL
- ✅ WebSocket pour updates temps réel

---

## 🤝 Contribution

1. Fork le projet
2. Créer une branche feature (`git checkout -b feature/amazing-feature`)
3. Commit les changements (`git commit -m 'Add amazing feature'`)
4. Push vers la branche (`git push origin feature/amazing-feature`)
5. Ouvrir une Pull Request

---

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](./LICENSE) pour plus de détails.

---

## 👨‍💻 Auteur

**Harifara** - [GitHub](https://github.com/Harifara)

---

## 📞 Support

Pour les questions ou issues, veuillez créer une issue sur [GitHub Issues](https://github.com/Harifara/Professional-statistical-analysis-platform-for-Aviator-game/issues).

---

## ⭐ Remerciements

- Django & Django REST Framework
- PostgreSQL
- React
- Redis & Celery
- Scikit-learn & XGBoost

