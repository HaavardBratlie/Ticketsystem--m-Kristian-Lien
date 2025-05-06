-- Oppretter tabell for kundehenvendelser
CREATE TABLE tickets (
    ticket_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    message TEXT NOT NULL,
    
    status ENUM('ikke påbegynt', 'under behandling', 'oppklart') DEFAULT 'ikke påbegynt',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Legger til en test rad i tickets-tabellen
INSERT INTO tickets (ticket_id, name, email, message, status) 
VALUES (1, 'Test Bruker', 'test@example.com', 'Dette er en testmelding.', 'ikke påbegynt');



-- Oppretter tabell for kundehenvendelser
CREATE TABLE tickets (
    ticket_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    hendvendelse TEXT NOT NULL,
    message TEXT NOT NULL,
    status ENUM('ikke påbegynt', 'under behandling', 'oppklart') DEFAULT 'ikke påbegynt',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- bruker for admin
INSERT INTO admin_users (brukernavn, passord) VALUES (%s, %s)", ("admin", "admin123"
