
enum GeopoliticalZone {
    NORTHEAST("Borno", "Yobe", "Bauchi", "Gombe", "Adamawa", "Taraba"),
    NORTHWEST("Kaduna", "Kano", "Katsina", "Sokoto", "Zamfara", "Kebbi", "Jigawa"),
    NORTHCENTRAL("Kwara", "Niger", "Plateau", "Benue", "Kogi", "Nasarawa", "FCT"),
    SOUTHSOUTH("Akwa Ibom", "Cross River", "Bayelsa", "Rivers", "Delta", "Edo"),
    SOUTHEAST("Abia", "Anambra", "Enugu", "Imo", "Ebonyi"),
    SOUTHWEST("Ogun", "Oyo", "Osun", "Ondo", "Ekiti", "Lagos");

    private final String[] states;

    GeopoliticalZone(String... states) {
        this.states = states;
    }

    public String[] getStates() {
        return states;
    }
}

