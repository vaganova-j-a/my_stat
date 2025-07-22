SELECT 
    s.id_st AS 'ID студента',
    CONCAT(s.surname, ' ', s.name, 
           CASE WHEN s.patronymic IS NOT NULL THEN CONCAT(' ', s.patronymic) ELSE '' END) AS 'Студент',
    g.group_name AS 'Группа',
    sp.name_specialty AS 'Направление',
    COUNT(m.id_m) AS 'Количество оценок',
    CASE 
        WHEN COUNT(m.id_m) > 0 THEN ROUND(AVG(m.mark), 2)
        ELSE NULL
    END AS 'Средний балл',
    SUM(CASE WHEN m.mark = 5 THEN 1 ELSE 0 END) AS 'Количество пятерок',
    SUM(CASE WHEN m.mark = 2 THEN 1 ELSE 0 END) AS 'Количество двоек'
FROM 
    student s
JOIN 
    study_group g ON s.group_id_g = g.id_g
JOIN 
    specialty sp ON g.specialty_id_spec = sp.id_spec
LEFT JOIN 
    mark m ON s.id_st = m.student_id_st
GROUP BY 
    s.id_st, s.surname, s.name, s.patronymic, g.group_name, sp.name_specialty
ORDER BY 
    CASE 
        WHEN COUNT(m.id_m) = 0 THEN 1
        ELSE 0
    END,
    AVG(m.mark) DESC,
    s.surname ASC;