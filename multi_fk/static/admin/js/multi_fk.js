/**
 * django-multi-fk
 * Copyright 2016 - Nathan Osman
 */

django.jQuery(function() {

    var $ = django.jQuery;

    // Each relationship form field needs to be added to a map that can be used
    // to find other fields using the same model and update them

    var map = {};

    $('select[data-model]').each(function() {
        var model = $(this).data('model');
        if (typeof map[model] === 'undefined') {
            map[model] = [];
        }
        map[model].push(this);
    });

    // Hook the window.dismissAddRelatedObjectPopup function in order to grab
    // a copy of the new object id and repr so that we can inject these into
    // the other fields as well

    var oldDismissAddRelatedObjectPopup = window.dismissAddRelatedObjectPopup;
    window.dismissAddRelatedObjectPopup = function(win, newId, newRepr) {

        // First invoke the original implementation
        oldDismissAddRelatedObjectPopup.apply(this, arguments);

        // TODO: only <select> is currently supported

        // Then obtain the model from the element and insert the data into the
        // other elements using the same model
        var elem = document.getElementById(window.windowname_to_id(win.name))
        if (elem) {
            var model = $(elem).data('model');
            if (model) {
                $.each(map[model], function() {
                    if (this !== elem) {
                        this.options[this.options.length] = new Option(newRepr, newId);
                    }
                });
            }
        }
    };
});
