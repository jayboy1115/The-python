
enum GeopoliticalZone {
    NORTH_EAST("Borno", "Yobe", "Bauchi", "Gombe", "Adamawa", "Taraba"),
    NORTH_WEST("Kaduna", "Kano", "Katsina", "Sokoto", "Zamfara", "Kebbi", "Jigawa"),
    NORTH_CENTRAL("Kwara", "Niger", "Plateau", "Benue", "Kogi", "Nasarawa", "FCT"),
    SOUTH_SOUTH("Akwa Ibom", "Cross River", "Bayelsa", "Rivers", "Delta", "Edo"),
    SOUTH_EAST("Abia", "Anambra", "Enugu", "Imo", "Ebonyi"),
    SOUTH_WEST("Ogun", "Oyo", "Osun", "Ondo", "Ekiti", "Lagos");

    private final String[] states;

    GeopoliticalZone(String... states) {
        this.states = states;
    }

    public String[] getStates() {
        return states;
    }
}

