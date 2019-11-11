// tests for functions in main.js

describe('changeChevronDirection function', function() {
    beforeEach(() => {
        setFixtures(`
            <i class="fa-chevron-down chevron"></i>
        `);
    });

    it('should remove class fa-chevron-down', function() {
        changeChevronDirection();
        expect($('.chevron')).not.toHaveClass('fa-chevron-down')
    });
    it('should add class fa-chevron-up', function() {
        changeChevronDirection();
        expect($('.chevron')).toHaveClass('fa-chevron-up')
    });
})