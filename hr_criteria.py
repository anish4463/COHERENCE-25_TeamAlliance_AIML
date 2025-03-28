def validate_hr_criteria(resume_data, required_skills, min_experience, min_10th, min_12th, min_cgpa):
    """
    Check if a candidate meets HR criteria.
    
    Parameters:
    - resume_data: Dictionary with candidate details (skills, experience, education).
    - required_skills: Set of skills required by HR.
    - min_experience: Minimum years of experience required.
    - min_10th: Minimum 10th grade percentage.
    - min_12th: Minimum 12th grade percentage.
    - min_cgpa: Minimum CGPA in graduation.

    Returns:
    - Boolean: True if candidate meets all criteria, False otherwise.
    """

    # Extracting candidate data
    skills = set(resume_data.get("skills", []))
    experience = resume_data.get("experience", 0)
    grade_10 = resume_data.get("grade_10", 0)
    grade_12 = resume_data.get("grade_12", 0)
    cgpa = resume_data.get("cgpa", 0)

    # Checking all conditions
    meets_criteria = (
        skills.issuperset(required_skills) and
        experience >= min_experience and
        grade_10 >= min_10th and
        grade_12 >= min_12th and
        cgpa >= min_cgpa
    )

    return meets_criteria

