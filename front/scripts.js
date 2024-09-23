const getList = async () => {
    let url = 'http://127.0.0.1:5000/students';
    fetch(url, {
      method: 'get',
    })
      .then((response) => response.json())
      .then((data) => {
        data.students.forEach(item => insertList(item.name, 
                                                  item.gender, 
                                                  item.attendanceRate,
                                                  item.studyHoursPerWeek,
                                                  item.previousGrade,
                                                  item.extracurricularActivities,
                                                  item.parentalSupport,
                                                  item.finalGrade
                                                ))
      })
      .catch((error) => {
        console.error('Error:', error);
      });
  }

  getList()