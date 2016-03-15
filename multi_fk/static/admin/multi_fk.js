/**
 * django-multi-fk
 * Copyright 2016 - Nathan Osman
 */

(function($) {

    // Each relationship form field needs to be added to a map that can be used
    // to find other fields using the same model and update them. Also, when
    // one of the fields receives an event, the appropriate action needs to be
    // taken on other fields as well.

    var map = {};

    $('[data-model]').each(function() {
        var $this = $(this),
            model = $this.data('model');
        if (typeof map[model] === 'undefined') {
            map[model] = [];
        }
        map[model].push($this);
    });

    console.log(map);

})(django.jQuery);
