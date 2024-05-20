SELECT s.student_id, s.student_name, AVG(g.grade) as average_grade
FROM students s 
JOIN grades g On s.student_id = g.student_id
WHERE g.subject_id = 1
GROUP BY s.student_id, s.student_name 
ORDER BY average_grade DESC
LIMIT 1;