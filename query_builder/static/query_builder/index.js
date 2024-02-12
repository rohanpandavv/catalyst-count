document.getElementById('queryBtn').addEventListener('click', function() {
    const keyword = document.getElementById('keyword').value;
    const industry = document.getElementById('industry').value;
    const yearFounded = document.getElementById('yearFounded').value;
    const city = document.getElementById('city').value;
    const state = document.getElementById('state').value;
    const country = document.getElementById('country').value;
    const employeesFrom = document.getElementById('employeesFrom').value;
    const employeesTo = document.getElementById('employeesTo').value;

    const queryParams = new URLSearchParams({
        keyword,
        industry,
        yearFounded,
        city,
        state,
        country,
        employeesFrom,
        employeesTo
    });
    
    fetch(`query_builder/api/count_data/?${queryParams}`)
        .then(response => response.json())
        .then(data => {
            const resultAlert = document.getElementById('resultAlert');
            resultAlert.classList.remove('alert-success', 'alert-danger');
            resultAlert.style.display = 'block';
            if (data.count == 0) {
                resultAlert.classList.add('alert-danger');
                resultAlert.textContent = 'No records found for the query.';
            } else {
                resultAlert.classList.add('alert-success');
                resultAlert.textContent = `${data.count} records found for the query`;
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
});

document.getElementById('resetBtn').addEventListener('click', function() {
    document.getElementById('keyword').value = "";
    document.getElementById('industry').value = '';
    document.getElementById('yearFounded').value = '';
    document.getElementById('city').value = '';
    document.getElementById('state').value = '';
    document.getElementById('country').value = '';
    document.getElementById('city').value = '';
    document.getElementById('employeesFrom').value = '';
    document.getElementById('employeesTo').value = ''

    document.getElementById('resultAlert').style.display = 'none';
});