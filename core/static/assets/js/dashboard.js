$(document).ready(function () {
    // to update orders and sales charts
    GraghQLAjax();

    // to update traffic and visit tables
    RESTAjax();
});


// Ajax functions to update chart and tables

function GraghQLAjax(params) {
    var query = JSON.stringify({
        query: `query {
            orders_month_report {
                month
                total
            }
            sales_month_report {
                month
                total_amount
            }
        }`
    });

    $.ajax({
        method: 'POST',
        url: '/graphql/',
        data: query,
        contentType: 'application/json',
        success: function (data) {
            var months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];

            // sales chart
            var sales_chart_data = [];
            $.each(data.data.sales_month_report, function (index, obj) {
                sales_chart_data.push(obj.total_amount);
            });
            SalesChart(sales_chart_data, months);

            // orders chart
            var orders_chart_data = [];
            $.each(data.data.orders_month_report, function (index, obj) {
                orders_chart_data.push(obj.total);
            });
            OrderChart(orders_chart_data, months);

        },
        error: function () {
            alert('Error occurred');
        }
    });
}

function RESTAjax() {
    $.ajax({
        method: 'GET',
        url: '/api/v1/visits/',
        success: function (data) {
            var html_template = '';
            $.each(data.results, function (index, obj) {
                html_template += '<tr>';
                html_template += '<th scope="row">' + obj.page_name + '</th>';
                html_template += '<td>' + obj.visitors + '</td>';
                html_template += '<td>' + obj.unique_users + '</td>';

                if (obj.bounce_rate_type === 1)
                    html_template += '<td><i class="fas fa-arrow-up text-success mr-3"></i>' + obj.bounce_rate + '%</td>';
                else
                    html_template += '<td><i class="fas fa-arrow-down text-warning mr-3"></i>' + obj.bounce_rate + '%</td>';

                html_template += '</tr>';

                $('#visitsInfo').find('tbody').html(html_template);
            });
        },
        error: function () {
            alert('Error occurred');
        }
    });


    $.ajax({
        method: 'GET',
        url: '/api/v1/traffics/',
        success: function (data) {
            var html_template = '';
            $.each(data.results, function (index, obj) {
                var bg_gradient = obj.rate_type === 1 ? "bg-gradient-success" : "bg-gradient-danger";
                html_template += '<tr>';
                html_template += '<th scope="row">' + obj.referral + '</th>';
                html_template += '<td>' + obj.visitors + '</td>';
                html_template += '<td><div class="d-flex align-items-center"><span class="mr-2">' + obj.rate + '%</span>';
                html_template += '<div><div class="progress">';
                html_template += '<div class="progress-bar ' + bg_gradient + '" role="progressbar" ' +
                    'aria-valuenow="' + obj.rate + '" aria-valuemin="0" aria-valuemax="100" ' +
                    'style="width: ' + obj.rate + '%;"></div>';
                html_template += '</div></div>';
                html_template += '</div></td>';
                html_template += '</tr>';

                $('#trafficsInfo').find('tbody').html(html_template);
            });
        },
        error: function () {
            alert('Error occurred');
        }
    });
}


// charts function

function SalesChart(data, labels) {
    // Variables
    var $chart = $('#chartSales');

    var salesChart = new Chart($chart, {
        type: 'line',
        options: {
            scales: {
                yAxes: [{
                    gridLines: {
                        lineWidth: 1,
                        color: Charts.colors.gray[900],
                        zeroLineColor: Charts.colors.gray[900]
                    },
                    ticks: {
                        callback: function (value) {
                            if (!(value % 10)) {
                                return '$' + value;
                            }
                        }
                    }
                }]
            },
            tooltips: {
                callbacks: {
                    label: function (item, data) {
                        var label = data.datasets[item.datasetIndex].label || '';
                        var yLabel = item.yLabel;
                        var content = '';

                        if (data.datasets.length > 1) {
                            content += '<span class="popover-body-label mr-auto">' + label + '</span>';
                        }

                        content += '<span class="popover-body-value">$' + yLabel + '</span>';
                        return content;
                    }
                }
            }
        },
        data: {
            labels: labels,
            datasets: [{
                label: 'Performance',
                data: data
            }]
        }
    });

    // Save to jQuery object
    $chart.data('chart', salesChart);
}

function OrderChart(data, labels) {
    var $chart = $('#chartOrders');

    var ordersChart = new Chart($chart, {
        type: 'bar',
        options: {
            scales: {
                yAxes: [{
                    gridLines: {
                        lineWidth: 1,
                        color: '#dfe2e6',
                        zeroLineColor: '#dfe2e6'
                    },
                    ticks: {
                        callback: function (value) {
                            if (!(value % 10)) {
                                //return '$' + value + 'k'
                                return value
                            }
                        }
                    }
                }]
            },
            tooltips: {
                callbacks: {
                    label: function (item, data) {
                        var label = data.datasets[item.datasetIndex].label || '';
                        var yLabel = item.yLabel;
                        var content = '';

                        if (data.datasets.length > 1) {
                            content += '<span class="popover-body-label mr-auto">' + label + '</span>';
                        }

                        content += '<span class="popover-body-value">' + yLabel + '</span>';

                        return content;
                    }
                }
            }
        },
        data: {
            labels: labels,
            datasets: [{
                label: 'Sales',
                data: data
            }]
        }
    });

    // Save to jQuery object
    $chart.data('chart', ordersChart);
}
