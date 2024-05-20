SELECT g.group_id, g.group_name, s2.subject_name, ROUND(AVG(grade)) as average_grade
FROM students s 
JOIN groups g ON s.group_id = g.group_id
JOIN grades g2 ON s.student_id = g2.student_id 
JOIN subjects s2 ON g2.subject_id = g2.subject_id
WHERE s2.subject_id = 1
GROUP BY g.group_id ;