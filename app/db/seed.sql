INSERT INTO regions (name) VALUES
  ('Северный учебный округ'),
  ('Приречный край'),
  ('Заозёрная область')
ON CONFLICT (name) DO NOTHING;

INSERT INTO disciplines (name, calc_format) VALUES
  ('Алгоритмическое программирование', 'A'),
  ('Продуктовое программирование', 'B'),
  ('Робототехника', 'V'),
  ('Программирование БАС', 'V'),
  ('Информационная безопасность', 'G')
ON CONFLICT (name) DO NOTHING;

INSERT INTO ranks (name, sort_order) VALUES
  ('Без разряда', 0),
  ('3 юношеский', 1),
  ('2 юношеский', 2),
  ('1 юношеский', 3),
  ('3 взрослый', 4),
  ('2 взрослый', 5),
  ('1 взрослый', 6),
  ('КМС', 7)
ON CONFLICT (name) DO NOTHING;

INSERT INTO calc_params (key, value, description) VALUES
  ('penalty_minutes', 20, 'Штрафные минуты за неверную попытку в формате А')
ON CONFLICT (key) DO NOTHING;
