SELECT s.student_id, s.student_name, t.teacher_name, s2.subject_name 
FROM students s 
JOIN grades g ON s.student_id = g.student_id 
JOIN subjects s2 ON s2.subject_id = g.subject_id 
JOIN teachers t ON t.teacher_id = s2.teacher_id 
WHERE s.student_id = 7 AND t.teacher_id = 4;
