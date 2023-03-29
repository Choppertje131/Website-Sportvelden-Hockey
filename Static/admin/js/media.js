$(function() {
    $('.related-widget-wrapper').on('DOMNodeInserted', function(e) {
        if ($(e.target).hasClass('related-widget-wrapper') && $(e.target).find('.file-upload').length) {
            $(e.target).find('.file-upload').on('click', function() {
                var modal = $(this).parent().parent().parent().parent();
                var iframe = modal.find('iframe');
                var iframeSrc = iframe.attr('src');
                var match = iframeSrc.match(/media\/([a-z0-9]+)/);
                var folderPk = match[1];
                iframe.attr('src', iframeSrc.replace(folderPk, ''));
                iframe.on('load', function() {
                    iframe.attr('src', iframeSrc);
                });
            });
        }
    });
});