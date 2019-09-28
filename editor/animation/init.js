//Dont change it
requirejs(['ext_editor_io', 'jquery_190', 'raphael_210'],
    function (extIO, $) {
        var $tryit;
        var io = new extIO({
            multipleArguments: true,
            functions: {
                python: 'reversed_permutation_index',
                js: 'reversedPermutationIndex'
            },
        });
        io.start();
    }
);
