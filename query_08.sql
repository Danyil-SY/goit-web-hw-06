SELECT t.teacher_id, t.teacher_name, ROUND(AVG(grade)) AS average_grade 
FROM teachers t
JOIN subjects s ON t.teacher_id = s.teacher_id
JOIN grades g ON s.subject_id = g.subject_id;