CREATE TABLE IF NOT EXISTS regions (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS disciplines (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL UNIQUE,
  calc_format CHAR(1) NOT NULL CHECK (calc_format IN ('A','B','V','G'))
);

CREATE TABLE IF NOT EXISTS ranks (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL UNIQUE,
  sort_order INT NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS calc_params (
  key TEXT PRIMARY KEY,
  value NUMERIC NOT NULL,
  description TEXT
);

CREATE TABLE IF NOT EXISTS users (
  id SERIAL PRIMARY KEY,
  email TEXT NOT NULL,
  full_name TEXT NOT NULL,
  password_hash TEXT NOT NULL,
  role TEXT NOT NULL CHECK (role IN ('athlete','trainer','admin')),
  status TEXT NOT NULL DEFAULT 'active' CHECK (status IN ('active','pending','blocked')),
  region_id INT REFERENCES regions(id),
  must_change_password BOOLEAN NOT NULL DEFAULT FALSE,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE UNIQUE INDEX IF NOT EXISTS users_email_uq ON users (lower(email));

CREATE TABLE IF NOT EXISTS athlete_profiles (
  user_id INT PRIMARY KEY REFERENCES users(id) ON DELETE CASCADE,
  birth_date DATE NOT NULL,
  gender CHAR(1) CHECK (gender IN ('M','F')),
  phone TEXT,
  photo_path TEXT,
  rank_id INT REFERENCES ranks(id),
  trainer_id INT REFERENCES users(id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS athlete_disciplines (
  user_id INT REFERENCES athlete_profiles(user_id) ON DELETE CASCADE,
  discipline_id INT REFERENCES disciplines(id),
  PRIMARY KEY (user_id, discipline_id)
);

CREATE TABLE IF NOT EXISTS consents (
  id SERIAL PRIMARY KEY,
  user_id INT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  document_version TEXT NOT NULL,
  accepted_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  guardian_consent_received BOOLEAN NOT NULL DEFAULT FALSE,
  guardian_confirmed_by INT REFERENCES users(id),
  guardian_confirmed_at TIMESTAMPTZ
);

CREATE TABLE IF NOT EXISTS competitions (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  discipline_id INT NOT NULL REFERENCES disciplines(id),
  region_id INT NOT NULL REFERENCES regions(id),
  city TEXT,
  event_date DATE NOT NULL,
  status TEXT NOT NULL DEFAULT 'planned'
    CHECK (status IN ('planned','running','finished','cancelled','postponed')),
  r_max NUMERIC NOT NULL CHECK (r_max > 0),
  params JSONB NOT NULL DEFAULT '{}'::jsonb,
  created_by INT REFERENCES users(id),
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS competition_criteria (
  id SERIAL PRIMARY KEY,
  competition_id INT NOT NULL REFERENCES competitions(id) ON DELETE CASCADE,
  name TEXT NOT NULL,
  weight NUMERIC NOT NULL CHECK (weight > 0 AND weight <= 1),
  max_value NUMERIC NOT NULL CHECK (max_value > 0)
);

CREATE TABLE IF NOT EXISTS results (
  id SERIAL PRIMARY KEY,
  competition_id INT NOT NULL REFERENCES competitions(id) ON DELETE RESTRICT,
  athlete_id INT NOT NULL REFERENCES athlete_profiles(user_id) ON DELETE RESTRICT,
  r_i NUMERIC NOT NULL,
  r_n NUMERIC,
  place INT,
  percentile NUMERIC,
  solved_count INT,
  penalty_time INT,
  penalty NUMERIC DEFAULT 0,
  details JSONB NOT NULL DEFAULT '{}'::jsonb,
  entered_by INT REFERENCES users(id),
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  UNIQUE (competition_id, athlete_id)
);

CREATE TABLE IF NOT EXISTS result_attempts (
  id SERIAL PRIMARY KEY,
  result_id INT NOT NULL REFERENCES results(id) ON DELETE CASCADE,
  attempt_no INT NOT NULL,
  points NUMERIC NOT NULL,
  penalty NUMERIC NOT NULL DEFAULT 0,
  time_min NUMERIC,
  UNIQUE (result_id, attempt_no)
);

CREATE TABLE IF NOT EXISTS result_criteria_scores (
  id SERIAL PRIMARY KEY,
  result_id INT NOT NULL REFERENCES results(id) ON DELETE CASCADE,
  criterion_id INT NOT NULL REFERENCES competition_criteria(id) ON DELETE CASCADE,
  avg_score NUMERIC NOT NULL,
  UNIQUE (result_id, criterion_id)
);

CREATE TABLE IF NOT EXISTS audit_log (
  id BIGSERIAL PRIMARY KEY,
  user_id INT REFERENCES users(id) ON DELETE SET NULL,
  action TEXT NOT NULL,
  entity TEXT,
  entity_id TEXT,
  details JSONB NOT NULL DEFAULT '{}'::jsonb,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS results_competition_idx ON results(competition_id);
CREATE INDEX IF NOT EXISTS results_athlete_idx ON results(athlete_id);
CREATE INDEX IF NOT EXISTS competitions_region_date_idx ON competitions(region_id, event_date);
CREATE INDEX IF NOT EXISTS audit_created_idx ON audit_log(created_at);
