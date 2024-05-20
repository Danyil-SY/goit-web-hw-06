SELECT t.teacher_id, t.teacher_name, ROUND(AVG(grade)) as average_grade
FROM grades g 
JOIN students s ON s.student_id = g.student_id 
JOIN subjects s2 ON s2.subject_id = g.subject_id 
JOIN teachers t ON t.teacher_id = s2.teacher_id 
WHERE g.student_id = 7 and t.teacher_id = 2
