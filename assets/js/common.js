$(document).ready(function() {
    $('a.abstract').click(function() {
        $(this).parent().parent().find(".abstract.hidden").toggleClass('open');
    });
    $('a.bibtex').click(function() {
        $(this).parent().parent().find(".bibtex.hidden").toggleClass('open');
    });
    $('a').removeClass('waves-effect waves-light');

    // Inline abstracts: hide the toggle when nothing is clamped, expand on click
    $('.abstract-inline').each(function() {
        var p = $(this).children('p')[0];
        if (p && p.scrollHeight <= p.clientHeight + 2) {
            $(this).children('.abstract-toggle').hide();
        }
    });
    $('.abstract-toggle').click(function() {
        var box = $(this).closest('.abstract-inline');
        box.toggleClass('expanded');
        var expanded = box.hasClass('expanded');
        $(this).text(expanded ? 'Show less' : 'Read more').attr('aria-expanded', expanded);
    });
});
