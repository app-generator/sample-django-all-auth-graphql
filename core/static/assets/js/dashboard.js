$(document).ready(function () {
    var sales_params = [];
    sales_params['url'] = '/graphql/';
    sales_params['query'] = JSON.stringify({
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
    GraghQLAjax(sales_params);

    RESTAjax();

});


// Ajax functions to update chart and tables

function GraghQLAjax(params) {
    $.ajax({
        method: 'POST',
        url: params['url'],
        data: params['query'],
        contentType: 'application/json',
        beforeSend: function (xhr) {
            xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
        },
        success: function (data) {
            var months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];

            var sales_chart_data = [];
            $.each(data.data.sales_month_report, function (index, obj) {
                sales_chart_data.push(obj.total_amount);
            });
            SalesChart(sales_chart_data, months);

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

function RestAjax(params) {

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
