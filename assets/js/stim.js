$(document).ready(function() {

    var data = [
        {wtv: 2.5, tgv: -2, type: 'ltp_gain_a'},
        {wtv: 4, tgv: 1, type: 'ltp_gain_b'},
        {wtv: -4, tgv: 1, type: 'ltp_loss_a'},
        {wtv: -3, tgv: -1.5, type: 'ltp_loss_b'},
        {wtv: 2, tgv: 4, type: 'shared_gain'},
        {wtv: -2, tgv: -4, type: 'shared_loss'}
    ]

    var margin = {top: 10, right: 70, bottom: 50, left: 60},
        plotWidth = 400,
        plotHeight = 400,
        width = plotWidth + margin.left + margin.right,
        height = plotHeight + margin.top + margin.bottom;

    var xScale = d3.scaleLinear()
        .domain([-5, 5])
        .range([0, plotWidth]);

    var yScale = d3.scaleLinear()
        .domain([-5, 5])
        .range([plotHeight, 0]);
        
    var colorScale = d3.scaleOrdinal()
        .domain(['ltp_gain_a', 'ltp_gain_b', 'ltp_loss_a', 'ltp_loss_b', 'shared_gain', 'shared_loss'])
        .range(['#7f8538', '#b1cf5f', '#b34342', '#f59d9e', '#f4b940', '#5ea4a1']);
        
    var xAxisGenerator = d3.axisBottom(xScale)
        .tickSize(0)
        .tickPadding(10);

    var yAxisGenerator = d3.axisLeft(yScale)
        .tickSize(0)
        .tickPadding(10);
        
    var svg = d3.select('#plot')
        .append('svg')
        .attr('width', width)
        .attr('height', height);
        
    var g = svg.append('g')
        .classed('plot', true)
        .attr('transform', 'translate(' + margin.left + ',' + margin.top + ')');
    
    g.append('g')
        .attr('transform', 'translate(0,' + plotHeight + ')')
        .call(xAxisGenerator);
        
    g.append('g')
        .call(yAxisGenerator);
        
    g.append('text')
        .classed('x axis', true)
        .attr('transform', 'translate(' + plotWidth / 2 + ',' + (plotHeight + 40) + ')')
        .text('Log Fold Change TBS effect in WtV');
        
    g.append('text')
        .classed('y axis', true)
        .attr('transform', 'translate(-35,' + plotHeight / 2 + ') rotate(-90)')
        .text('Log Fold Change TBS effect in TgV');
        
    g.append('line')
        .attr('x1', plotWidth / 2)
        .attr('y1', 0)
        .attr('x2', plotWidth / 2)
        .attr('y2', plotHeight);
        
    g.append('line')
        .attr('x1', 0)
        .attr('y1', plotHeight / 2)
        .attr('x2', plotWidth)
        .attr('y2', plotHeight / 2);
        
    g.append('line')
        .classed('divider', true)
        .attr('x1', 0)
        .attr('y1', plotHeight)
        .attr('x2', plotWidth)
        .attr('y2', 0);
        
    g.append('g')
        .classed('dots', true)
        .selectAll('circle')
        .data(data)
        .enter()
        .append('circle')
        .attr('cx', function (d) { return xScale(d.wtv); } )
        .attr('cy', function (d) { return yScale(d.tgv); } )
        .attr('r', 4)
        .attr('fill', function (d) { return colorScale(d.type); });
    
    var labels = g.append('g')
        .classed('labels', true)
        .style('opacity', 0);
    
    labels.append('text')
        .attr('transform', 'translate(' + plotWidth * 3 / 4 + ',' + plotHeight * 3 / 4 + ')')
        .style('fill', '#98AA4C')
        .text('LTP-dependent gain');
    
    labels.append('text')
        .attr('transform', 'translate(' + plotWidth / 4 + ',' + plotHeight / 4 + ')')
        .style('fill', '#D47070')
        .text('LTP-dependent loss');
    
    labels.append('text')
        .attr('transform', 'translate(' + plotWidth * 3 / 4 + ',' + plotHeight / 4 + ')')
        .style('fill', '#f4b940')
        .text('Shared gain');
    
    labels.append('text')
        .attr('transform', 'translate(' + plotWidth / 4 + ',' + plotHeight * 3 / 4 + ')')
        .style('fill', '#5ea4a1')
        .text('Shared loss');
    
    $('.btn').on('click', function() {
        var $this = $(this),
            $value = $this.data('value');

        if ($this.hasClass('btn-primary')) return;
        
        $this.parent().find('.btn-primary').removeClass('btn-primary').addClass('btn-secondary');
        $this.removeClass('btn-secondary').addClass('btn-primary');
        
        if ($value === 'tgv') {
            g.selectAll('.dots circle')
                .transition()
                .duration(500)
                .attr('cy', function(d) { return yScale(d.tgv); });
                
            g.select('.divider')
                .transition()
                .duration(500)
                .attr('x1', 0)
                .attr('y1', plotHeight)
                .attr('x2', plotWidth)
                .attr('y2', 0);
                
            g.select('.y')
                .transition()
                .duration(200)
                .style('opacity', 0)
                .on('end', function() {
                    d3.select(this).text('Log Fold Change TBS effect in TgV');
                })
                .transition()
                .duration(200)
                .style('opacity', 1);
                
            g.select('.labels')
                .transition()
                .duration(300)
                .style('opacity', 0);
        } else if ($value === 'tgv_wtv') {
            g.selectAll('.dots circle')
                .transition()
                .duration(500)
                .attr('cy', function(d) { return yScale(d.tgv - d.wtv); });
                
            g.select('.divider')
                .transition()
                .duration(500)
                .attr('x1', 0)
                .attr('y1', plotHeight / 2)
                .attr('x2', plotWidth)
                .attr('y2', plotHeight / 2);
                
            g.select('.y')
                .transition()
                .duration(200)
                .style('opacity', 0)
                .on('end', function() {
                    d3.select(this).text('Log Fold Change TBS effect in (TgV - WtV)');
                })
                .transition()
                .duration(200)
                .style('opacity', 1);
                
            g.select('.labels')
                .transition()
                .delay(200)
                .duration(300)
                .style('opacity', 1);
        }
    })

});
