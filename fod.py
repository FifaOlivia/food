{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "4f51b5bb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Importation terminée !\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd \n",
    "from sqlalchemy import create_engine\n",
    "\n",
    "# Connexion à la base de données db_food\n",
    "engine = create_engine('mysql+pymysql://root:@localhost/db_food')\n",
    "\n",
    "\n",
    "# Lire les données du fichier onlinefood.CSV\n",
    "df = pd.read_csv('onlinefoods.csv', sep=',', quotechar=\"'\", encoding='utf8')\n",
    "\n",
    "# load les données de csv vers la table online_food dans mysql\n",
    "df.to_sql('online_food', con=engine, index=False, if_exists='append')\n",
    "\n",
    "print(\"Importation terminée !\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5fda0d86",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
