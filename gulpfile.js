const gulp = require('gulp');
const babel = require('gulp-babel');

gulp.task('default', () =>
    gulp.src('ui/static/ui/results/src')
        .pipe(babel({
            presets: ['@babel/env']
        }))
        .pipe(gulp.dest('ui/static/ui/results'))
);