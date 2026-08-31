$(document).ready(function() {
  
    // Tab selection
    $('.tabset div').on('click', function() {
        var sel = $(this).data('tab');
        $('.tab, .tabset div').removeClass('active');
        $('#' + sel).addClass('active');
        $(this).addClass('active');
    });
    
    // Cell types
    // The page picks its taxonomy via data-src; v1.0 and v2.0 use different ones.
    $.getJSON($('#plot').data('src') || '/assets/data/cell_types.json', genCellTypes);

    function genCellTypes(data) {

        // Levels of the hierarchy below root, outermost last. The last one is
        // drawn as radial leaf labels, the rest as arcs.
        var levels = data.levels || ['class', 'neighborhood', 'subclass'],
            leafDepth = levels.length;

        // Canvas and the margin reserved for leaf labels. Taxonomies with
        // longer labels need more of both; the svg scales to fit its column.
        var width = data.size || 700,
            height = width,
            cx = width * 0.5,
            cy = height * 0.5,
            radius = Math.min(width, height) / 2 - (data.margin || 60);

        var lineGen = d3.lineRadial()
            .angle(function(d) { return d.x * Math.PI / 180; })
            .radius(function(d) { return d.y; });

        var numLeaves = d3.hierarchy(data).descendants().filter(function(d) {
            return d.depth == leafDepth;
        }).length;

        // Leaf colours interpolate across the ramp; fall back to the inner
        // nodes' own colours if a taxonomy doesn't define one.
        var ramp = data.ramp || data.children.map(function(d) { return d.color; });

        var colorGen = d3.scaleOrdinal(
            d3.quantize(d3.interpolateRgbBasis(ramp), numLeaves)
        );
        
        // Append to plot
        var svg = d3.select('#plot')
            .append('svg')
            .attr('width', width)
            .attr('height', height)
            .attr('viewBox', [-cx, -cy, width, height])
            .classed('depth-' + leafDepth, true);
            
        var g = svg.append('g')
            .attr('transform', 'rotate(45)');
            
        var info = svg.append('g')
            .classed('info-box', true)
            .attr('transform', 'translate(0,-' + (radius + 10) + ')');
            
        // Add info text
        info.append('text')
            .classed('title', true)
            .text('Cell types')
            
        info.append('text')
            .classed('subtitle', true)
            .attr('transform', 'translate(0, 22)')
            .text('Hover over cell type below for more info.')
            
        var cellInfo = info.append('g')
            .classed('cell-type', true)
            .attr('transform', 'translate(0, 110)');
            
        cellInfo.append('text')
            .classed('name', true);
            
        cellInfo.append('text')
            .classed('level', true)
            .attr('transform', 'translate(0, 20)');
            
        cellInfo.append('text')
            .classed('markers', true)
            .attr('transform', 'translate(0, 40)');
            
        // Create cluster layout
        var cluster = d3.cluster()
            .size([270, radius]);
        
        // Give data to cluster layout
        var root = d3.hierarchy(data);
        cluster(root);
    
        // Add links
        g.append('g')
            .classed('links', true)
            .selectAll('path')
            .data(root.links().filter(function(d) { return d.source.data.name !== 'root'; }))
            .enter()
            .append('path')
            .attr('d', function (d) {
                return lineGen([d.source, d.target])
            })
            .each(function(d) { d.target.linkNode = this; });
            
        // Add nodes
        var nodes = g.append('g')
            .classed('nodes', true);
            
        nodes.selectAll('text')  // outermost level
            .data(root.descendants().filter(function(d) { return d.depth == leafDepth; }))
            .enter()
            .append('text')
            .attr('dy', '0.31em')
            .attr('fill', colorGen)
            .attr('transform', function(d) { return 'rotate(' + d.x + ', 0, 0) translate(0, ' + -(d.y + 2) + ') rotate(' + (d.x < 135 ? -90 : 90) + ', 0, 0)'; })
            .attr('text-anchor', function(d) { return d.x < 135 ? 'start' : 'end'; })
            .text(function(d) { return d.data.name; })
            .each(function(d, i) { d.data.color = colorGen(i); })
            .on('mouseover', mouseovered(true))
            .on('mouseout', mouseovered(false));
            
        var classes = nodes.selectAll('g')  // inner levels
            .data(root.descendants().filter(function(d) { return d.depth && d.depth < leafDepth; }))
            .enter()
            .append('g');
        
        classes.append('path')
            .attr('d', function(d) {
                var isFlipped = true;  // 90 < d.x && d.x < 270
                return d3.arc()({
                    innerRadius: 0,
                    outerRadius: isFlipped ? d.y - 5 : d.y + 5,
                    startAngle: isFlipped ? d.x * Math.PI / 180 + 1 : d.x * Math.PI / 180 - 1,
                    endAngle: isFlipped ? d.x * Math.PI / 180 - 1 : d.x * Math.PI / 180 + 1
                })
            })
            .attr('id', function(d, i) { return 'path-' + i; });
        
        classes.append('text')
            .attr('dy', '0.5em')
            .attr('fill', function(d) { return d.data.color; })
            .each(function(d) { var p = this; d.children && d.children.forEach(function(c) { c.parentNode = p; }); })
            .on('mouseover', mouseovered(true))
            .on('mouseout', mouseovered(false))
            .append('textPath')
            .attr('xlink:href', function(d, i) { return '#path-' + i; })
            .attr('startOffset', '25%')
            .attr('text-anchor', 'middle')
            .text(function(d) { return d.data.name; });
            
        function mouseovered(active) {
            return function(event, d) {
                // Display cell type info
                d3.select('.info-box .cell-type').classed('hidden', !active);
                d3.select('.info-box .name').text(d.data.full_name || d.data.name).attr('fill', d.data.color);
                d3.select('.info-box .level').text(levels[d.depth - 1]);
                d3.select('.info-box .markers').text(d.data.markers);
                
                // Highlight selected cell type
                d3.selectAll('.nodes text, .links path').classed('inactive', active);
                d3.select(this).classed('label--active', active);
                do {
                  d3.select(d.linkNode).classed('link--active', active);
                  d3.select(d.parentNode).classed('label--active', active);
                } while (d = d.parent);
            };
        }
    }

});
