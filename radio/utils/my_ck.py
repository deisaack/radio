CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
CKEDITOR_RESTRICT_BY_USER = True
CKEDITOR_ALLOW_NONIMAGE_FILES = False


# CKEDITOR_RESTRICT_BY_USER = True
MATHJAX_ENABLED=True
MATHJAX_LOCAL_PATH = 'js/libs/mathjax/'


CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moonocolor',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
            {'name': 'forms',
             'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
                       'HiddenField']},
            '/',
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
                       'Language']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert',
             'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
            '/',
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks', 'Math']},
            # {'name': 'about', 'items': ['About']},
            '/',  # put this to force next toolbar on new line
            {'name': 'yourcustomtools', 'items': [
                # put the name of your editor.ui.addButton here
                'Preview', 'Youtube', 'pbckcode', 'rotateLeft', 'ckawesome',
                'Maximize', 'CodeSnippet', 'EqnEditor', 'Emojione',
                # 'Glyphicons',

            ]},
            { 'name': 'Icons', 'items': ['Image', 'Chart']},
            {'name' : 'texttransform', 'items': ['TransformTextToUppercase', 'TransformTextToLowercase', 'TransformTextCapitalize',
                     'TransformTextSwitcher']}

            # { 'name': 'glyphs', 'items': [ 'Glyphicons', 'Source' ] }
        ],
        'toolbar': 'YourCustomToolbarConfig',
        'fontawesomePath': '/static/css/libs/font-awesome/css/font-awesome.min.css',
        # put selected toolbar config here
        # 'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
        # 'height': 291,
        # 'width': '100%',
        # 'filebrowserWindowHeight': 725,
        # 'filebrowserWindowWidth': 940,
        # 'toolbarCanCollapse': True,
        # 'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
        'codeSnippet_theme': 'xcode',
        # 'mathJaxClass': 'my-math',
        'contentsCss': '/static/css/libs/bootstrap/css/bootstrap.min.css',
        # 'contentsCss':'https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css',
        'allowedContent': True,
        # 'mathJaxLib' : '/static/js/libs/MathJax.js',
        'tabSpaces': 4,
        'youtube_responsive' : True,
        'scayt_autoStartup' : True,
        'imageResize' : [{
            'maxWidth' : 400,
            'maxHeight' : 300,
        }],


        'extraPlugins': ','.join([
            'chart',
            'texttransform',
            'uploadimage',
            'ckawesome',
            'lineheight',
            # 'glyphicons',
            'fontawesome',
            # 'pbckcode',
            # 'eqneditor',
            'autocorrect',
            'imagerotate',
            'menubutton',
            'autolink',
            'wordcount',
            'filetools',
            'htmlwriter',
            'undo',
            'pastefromexcel',
            'codesnippet',
            'imageresize',
            'panel',
            'emojione',
            'uploadfile',
            'uploadwidget',
            'toolbar',
            'notificationaggregator',
            'notification',
            'button',
            'filetools',
            'clipboard',
            'widget',
            'widgetselection',
            'selectall',
            'lineutils',
            'link',
            'fakeobjects',
            'autogrow',
            'tableresize',
            'tabletools',
            'table',
            'colordialog',
            'dialogadvtab',
            'contextmenu',
            'menu',
            'floatpanel',
            'div',
            'autolink',
            'autoembed',
            'embedsemantic',
            'autogrow',
            'smiley',
            'font',
            'youtube',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath',
            # 'devtools',
            # 'image2',
            # 'bootstrapVisibility',
            # 'bt_table',
            # 'bgimage',
            # 'imageresponsive',
            # the upload image feature
            # your extra plugins here
            # 'mathjax',
            # 'embedbase',
            # 'ckeditortablecellsselection',
            # 'btquicktable',

        ]),
    }
}
