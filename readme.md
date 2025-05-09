# Ticketsystem for Fjell Bedriftsløsninger

Dette er et ticketsystem for Fjell Bedriftsløsninger, som lar brukere sende inn henvendelser, sjekke status på henvendelser, og administrere henvendelser som administrator.

## Funksjonalitet

### 1. **Hjemmeside**
- **URL:** `/`
- **Beskrivelse:** Velkomstsiden for Fjell Bedriftsløsninger. Her finner du generell informasjon om tjenestene som tilbys.

### 2. **Send inn henvendelse**
- **URL:** `/send`
- **Beskrivelse:** Lar brukere sende inn en henvendelse ved å fylle ut et skjema med navn, e-post, type henvendelse og en melding.
- **Hvordan bruke:**
  1. Gå til `/send`.
  2. Fyll ut skjemaet med nødvendig informasjon.
  3. Klikk på "Send inn" for å sende henvendelsen.
  4. Etter innsending blir du videresendt til en bekreftelsesside med detaljer om henvendelsen.

### 3. **Status på henvendelser**
- **URL:** `/status`
- **Beskrivelse:** Viser en oversikt over alle henvendelser som er sendt inn. Her kan man se navn, type henvendelse, status og saksnummer, men ikke detaljer om henvendelsen.
- **Hvordan bruke:**
  1. Gå til `/status`.
  2. Se oversikten over alle henvendelser.

### 4. **Administratorinnlogging**
- **URL:** `/admin`
- **Beskrivelse:** Lar administratorer logge inn for å få tilgang til administrasjonsfunksjoner.
- **Hvordan bruke:**
  1. Gå til `/admin`.
  2. Fyll inn brukernavn og passord.
  3. Klikk på "Logg inn" for å få tilgang til administratorfunksjoner.

### 5. **Administrasjon av henvendelser**
- **URL:** `/henvendelser`
- **Beskrivelse:** Kun tilgjengelig for administratorer. Viser en liste over alle henvendelser med mulighet til å se detaljer, endre status og slette henvendelser.
- **Hvordan bruke:**
  1. Logg inn som administrator via `/admin`.
  2. Gå til `/henvendelser` for å se alle henvendelser.
  3. Klikk på "Detaljer" for å se full informasjon om en henvendelse.
  4. Endre status ved å velge en ny status fra rullegardinmenyen og klikke "Oppdater status".
  5. Slett en henvendelse ved å klikke på "Slett" og bekrefte handlingen.

### 6. **Bekreftelsesside**
- **URL:** `/bekreft`
- **Beskrivelse:** Vises etter at en henvendelse er sendt inn. Gir en oppsummering av henvendelsen, inkludert saksnummer.
- **Hvordan bruke:**
  1. Etter å ha sendt inn en henvendelse via `/send`, blir du automatisk videresendt til denne siden.

### 7. **Detaljer om henvendelse**
- **URL:** `/detaljer/<ticket_id>`
- **Beskrivelse:** Kun tilgjengelig for administratorer. Viser full informasjon om en spesifikk henvendelse.
- **Hvordan bruke:**
  1. Logg inn som administrator via `/admin`.
  2. Gå til `/henvendelser` og klikk på "Detaljer" for ønsket henvendelse.

### 8. **Logg ut**
- **URL:** `/logout`
- **Beskrivelse:** Logger ut administratoren og fjerner tilgang til administrasjonsfunksjoner.
- **Hvordan bruke:**
  1. Klikk på "Logg ut" i navigasjonsmenyen etter å ha logget inn som administrator.

## Teknisk informasjon

- **Backend:** Flask
- **Database:** MySQL
- **Frontend:** HTML, CSS
- **Krav:** 
  - Python 3.x
  - MySQL-server
  - Flask-biblioteket (`pip install flask mysql-connector-python`)

## Oppsett

1. **Installer avhengigheter:**
   ```bash
   pip install flask mysql-connector-python
2. **Start applikasjonen:**
   ```bash
   python app.py
