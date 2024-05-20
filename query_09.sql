SELECT s.student_id, s.student_name, s2.subject_name 
FROM students s 
JOIN grades g ON s.student_id = g.student_id 
JOIN subjects s2 ON g.subject_id = s2.subject_id
WHERE s.student_id = 7
GROUP BY s2.subject_id 
